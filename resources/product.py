from flask import Response, json, jsonify, make_response
from flask_jwt_extended import current_user, jwt_required
from flask_restful import Resource, reqparse
from common.utils import get_asin_from_cache, set_asin_to_cache, get_asin_from_url
from crawler.SpiderifyWrapper import SpiderifyWrapper
from common.db import db
from models.Product import ProductModel
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
            asin=asin, user_id=current_user.id
        ).one_or_none()
        if product:
            return_product = {
                "asin": product.asin,
                "name": product.name,
                "price": product.price,
                "rating": product.rating,
                "description": product.description,
            }
            return make_response(jsonify(return_product), 200)
        else:
            return make_response(
                jsonify({"message": "Failed To Find Such Product"}), 404
            )

    def post(self):
        pass

    def put(self):
        pass

    @jwt_required()
    def delete(self, asin):
        product = ProductModel.query.filter_by(
            asin=asin, user_id=current_user.id
        ).one_or_none()
        if product is None:
            return make_response(
                jsonify({"message": "This Product is Already Deleted"}), 404
            )
        product.delete_from_db()
        return make_response(jsonify({"message": "Product Has Been Deleted"}), 200)


# ("/products") - -> class ProductList - -> only GET
class ProductsList(Resource):
    @jwt_required()
    def get(self):
        user_products = current_user.products
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
        # First it looks for the data in redis cache
        product_asin = get_asin_from_url(str(data["url"]))
        resp = get_asin_from_cache(key=product_asin)
        # If cache is found then serves the data from cache
        if resp is not None:
            resp = json.loads(resp)
            resp["cache"] = True
            return resp
        else:
            # If cache is not found then sends request to the RainForest API
            spider = SpiderifyWrapper(str(data["url"]))
            spider_data = spider.start_amazon_spider()
            if spider_data is None:
                return make_response(jsonify({"message": "Failed to Scrap Data"}))

            message = json.dumps(spider_data)
            is_cached = set_asin_to_cache(key=spider_data["ASIN"], value=message)
            if is_cached is True:
                 resp = Response(message, status=200, mimetype="application/json")

            newproduct = ProductModel(
                asin=spider_data["ASIN"],
                name=spider_data["PRODUCT_NAME"],
                price=spider_data["PRICE"],
                rating=float(spider_data["RATING"]),
                description=spider_data["PRODUCT_DESCRIPTION"],
                user_id=current_user.id,
            )

            for review in spider_data["REVIEWS"]:
                list_review = []
                new_review = CommentModel(
                    author="",
                    title=review["title"],
                    content=review["content"],
                    is_verified=review["verified_purchase"],
                    variant="",
                    rating=review["rating"],
                    date="U/N",
                    sentiment=review["sentiment"],
                    summarized_content=review["Summary"],
                )
                newproduct.comments.append(new_review)
                list_review.append(new_review)

            db.session.add(newproduct)
            db.session.add_all(list_review)
            db.session.commit()
        return resp


class LastProducts(Resource):
    def get(self):
        number_of_products = ProductModel.query.count()
        products = []
        for _ in range(10):
            product_obj = ProductModel.query.filter_by(
                id=randint(1, number_of_products)
            )
            if product_obj is None:
                continue
            products.append(product_obj)
        return make_response(jsonify({"products": products}), 200)
