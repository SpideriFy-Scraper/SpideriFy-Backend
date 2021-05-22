from flask_restful import Resource, reqparse
from models.Product import ProductModel
from models.User import UserModel
from common.db import db
from crawler.SpiderifyWrapper import SpiderifyWrapper
from flask import jsonify, Response, json
from flask_jwt_extended import jwt_required, current_user



# @jwt_required()

# @jwt.user_identity_loader
# def user_identity_lookup(user):
#     return user.id

# ("/product/<string:asin>") - -> class Product - -> GET, POST, DELETE, PUT


class Product(Resource):
    def get(self, asin):
        """
        Return the product row in the Product table using asin
        """
        # db.session.query(UserModel).join(ProductModel).filter(username, asin)
        # product = ProductModel.query.filter_by(asin=asin)
        # return
        pass

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass


# ("/products") - -> class ProductList - -> only GET
@jwt_required()
class ProductsList(Resource):
    def get(self):
        user_products = ProductModel.query.join(UserModel, ProductModel.user_id == UserModel.id) \
            .filter(ProductModel.user_id == current_user.id).all()
        list_product = []
        for product in user_products:
            data = {
                'asin': product.asin,
                'name': product.name,
                'price': product.price,
                'rating': product.rating,
                'description': product.description,
            }
            list_product.append(data)
        return jsonify({'products': list_product}), 200





# ("/new-product") -> body -> url: str = URL // / JWT = ?


class NewProduct(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('url', type=str, required=True,
                        help="This Is The Base Product URL")

    def post(self):
        data = NewProduct.parser.parse_args()
        spider = SpiderifyWrapper(str(data["url"]))
        spider_data = spider.start_amazon_spider()
        message = json.dumps(spider_data)
        resp = Response(message, status=200, mimetype='application/json')
        return resp


class LastProducts(Resource):
    pass
