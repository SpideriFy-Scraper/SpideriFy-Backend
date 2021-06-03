from flask import Response, json, jsonify, make_response
from flask_jwt_extended import current_user, jwt_required
from flask_restful import Resource, reqparse

from crawler.SpiderifyWrapper import SpiderifyWrapper
from common.db import db
from models.Product import ProductModel
from models.User import UserModel
from models.Comment import CommentModel
from random import randint


# ("/product/<string:asin>") - -> class Product - -> GET, POST, DELETE, PUT
class Product(Resource):
    @jwt_required()
    def get(self, asin):
        """
        Return the product row in the Product table using asin
        """
        product = ProductModel.query.filter_by(
            asin=asin, user_id=current_user.id).one_or_none()
        if product:
            return_product = {
                "asin": product.asin,
                "name": product.name,
                "price": product.price,
                "rating": product.rating,
                "description": product.description,
            }
            reviews_list = CommentModel.query.filter_by(
                product_id=product.id)
            reviews = []
            for review in reviews_list:
                data = {
                    "author": review.author,
                    "title": review.title,
                    "content": review.content,
                    "verified": review.is_verified,
                    "variant": review.variant,
                    "rating": review.rating,
                    "date": review.date,
                    "sentiment": review.sentiment,
                    "summarized content": review.summerized_content,
                }
                reviews.append(data)
            return_product["reviews"] = reviews
            return make_response(jsonify(return_product), 200)
        else:
            return make_response(jsonify({"message": "Failed To Find Such Product"}), 404)


    def post(self):
        pass

    def put(self):
        pass

    @jwt_required()
    def delete(self, asin):
        product = ProductModel.query.filter_by(
            asin=asin, user_id=current_user.id).one_or_none()
        if product is None:
            return make_response(jsonify({"message": "This Product is Already Deleted"}), 404)
        product.delete_from_db()
        return make_response(jsonify({"message": "Product Has Been Deleted"}), 200)


# ("/products") - -> class ProductList - -> only GET
class ProductsList(Resource):
    @jwt_required()
    def get(self):
        user_products = (
            ProductModel.query.join(
                UserModel, user_id=UserModel.id)
            .filter_by(user_id=current_user.id)
            .all()
        )
        if user_products is None:
            return make_response(jsonify({"message": "Product List is Empty"}), 204)
        list_product = []
        for product in user_products:
            data = {
                "asin": product.asin,
                "name": product.name,
                "price": product.price,
                "rating": product.rating,
                "description": product.description,
            }
            list_product.append(data)
        return make_response(jsonify({"products": list_product}), 200)


# ("/new-product") -> body -> url: str = URL // / JWT = ?


class NewProduct(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "url", type=str, required=True, help="This Is The Base Product URL"
    )
    @jwt_required()
    def post(self):
        data = NewProduct.parser.parse_args()
        spider = SpiderifyWrapper(str(data["url"]))
        spider_data = spider.start_amazon_spider()
        if spider_data is None:
            return make_response(jsonify({"message":"Failed to Scrap Data"}))
        message = json.dumps(spider_data)
        resp = Response(message, status=200, mimetype="application/json")
        newproduct = ProductModel(
            asin=spider_data["ASIN"],
            name=spider_data["PRODUCT_NAME"],
            price=spider_data["PRICE"],
            rating=spider_data["RATING"],
            description=spider_data["PRODUCT_DESCRIPTION"],
            user_id=current_user.id
        )

        for review in spider_data["REVIEWS"]:
            list_review = []
            new_review = CommentModel(
                author=review["author"],
                title=review["title"],
                content=review["content"],
                is_verified=review["verified"],
                variant=review["variant"],
                rating=review["rating"],
                date=review["date"]
            )
            newproduct.comments.append(new_review)
            list_review.append(new_review)

        db.session.add(newproduct)
        db.session.add_all(list_review)
        db.session.commit()
        return resp


class LastProducts(Resource):
    def get(self):
        number_of_products = ProductModel.query.filter_by(
            ProductModel.id).count()
        products = []
        for _ in range(10):
            product_obj = ProductModel.query.filter_by(
                id = randint(1, number_of_products))
            if product_obj is None:
                continue
            products.append(product_obj)
        return make_response(jsonify({"products": products}), 200)
