from flask import Response, json, jsonify
from flask_jwt_extended import current_user, jwt_required
from flask_restful import Resource, reqparse

from common.db import db
from crawler.SpiderifyWrapper import SpiderifyWrapper
from models.Product import ProductModel
from models.User import UserModel
from models.Comment import CommentModel
from random import randint

# ("/product/<string:asin>") - -> class Product - -> GET, POST, DELETE, PUT


class Product(Resource):

    @jwt_required
    def get(self, asin):
        """
        Return the product row in the Product table using asin
        """
        product = ProductModel.query.filter_by(
            asin=asin, user_id=current_user.id).one_or_none()  # is it only one obj???????????
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
            return jsonify(return_product), 200
        else:
            return jsonify({"message": "Failed To Find Such Product"}), 404
        # db.session.query(UserModel).join(ProductModel).filter(username, asin)
        # product = ProductModel.query.filter_by(asin=asin)
        # return

    def post(self):
        pass

    def put(self):
        pass

    @jwt_required
    def delete(self, asin):
        product = ProductModel.query.filter_by(
            asin=asin, user_id=current_user.id).one_or_none()
        if product is None:
            return jsonify({"message": "This Product is Already Deleted"}), 404
        product.delete_from_db()
        return jsonify({"message": "Product Has Been Deleted"}), 200
        # session.delete(product)
        # session.delete(reviews)


# ("/products") - -> class ProductList - -> only GET
class ProductsList(Resource):
    @jwt_required
    def get(self):
        user_products = (
            ProductModel.query.join(
                UserModel, user_id=UserModel.id)
            .filter_by(user_id=current_user.id)
            .all()
        )
        if user_products is None:
            return jsonify({"message": "Product List is Empty"}), 204
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
        return jsonify({"products": list_product}), 200


# ("/new-product") -> body -> url: str = URL // / JWT = ?


class NewProduct(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "url", type=str, required=True, help="This Is The Base Product URL"
    )

    def post(self):
        data = NewProduct.parser.parse_args()
        spider = SpiderifyWrapper(str(data["url"]))
        spider_data = spider.start_amazon_spider()
        message = json.dumps(spider_data)
        resp = Response(message, status=200, mimetype="application/json")
        newproduct = ProductModel(
            asin=spider_data["ASIN"],
            name=spider_data["PRODUCT_NAME"],
            price=spider_data["PRICE"],
            rating=spider_data["RATING"],
            description=spider_data["PRODUCT_DESCRIPTION"],
            user_id=current_user.id,
        )
        newproduct.save_to_db()
        for review in spider_data["REVIEWS"]:
            new_review = CommentModel(
                author=review["author"],
                title=review["title"],
                content=review["content"],
                is_verified=review["verified"],
                variant=review["variant"],
                rating=review["rating"],
                date=review["data"],
                product_id=newproduct.id
            )
            new_review.save_to_db()
        return resp


class LastProducts(Resource):
    def get(self):
        number_of_products = ProductModel.query.filter_by(
            ProductModel.id).count()
        products = []
        for _ in range(10):
            products.append(ProductModel.query.filter(
                ProductModel.id == randint(1, number_of_products)))
        return jsonify({"products": products}), 200
