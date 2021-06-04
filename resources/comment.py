from flask import Response, make_response, jsonify
from flask_jwt_extended import jwt_required, current_user
from flask_restful import Resource
from models.Product import ProductModel


# ("/product/<string:asin>/comments")--> class CommentsList - -> GET
class CommentsList(Resource):
    @jwt_required()
    def get(self, asin):
        """
        Return all Comments of a given product using asin
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
            reviews_list = product.comments
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
                    "summarized content": review.summarized_content,
                }
                reviews.append(data)
            return_product["reviews"] = reviews
            return make_response(jsonify(return_product), 200)
        else:
            return make_response(
                jsonify({"message": "Failed To Find Such Product"}), 404
            )
