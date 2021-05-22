from flask import Flask
from flask_restful import Api
from resources.product import Product, ProductsList, NewProduct, LastProducts
from resources.comment import CommentsList
from resources.user import Login, Register
from common.db import db
from flask_cors import CORS
from flask_jwt_extended import JWTManager


app = Flask(__name__)
jwt = JWTManager(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

if app.config['ENV'] == 'production':
    app.config.from_object('config.ProductionConfig')
elif app.config['ENV'] == 'development':
    app.config.from_object('config.DevelopmentConfig')
else:
    app.config.from_object('config.TestingConfig')

api = Api(app)

api.add_resource(NewProduct, '/api/v1/new-product')
api.add_resource(Register, '/api/v1/user/register')
api.add_resource(Login, '/api/v1/user/login')
api.add_resource(ProductsList, '/api/v1/products')
api.add_resource(Product, '/api/v1/product/<string:asin>')
api.add_resource(CommentsList, '/api/v1/product/<string:asin>/comments')
api.add_resource(LastProducts, '/api/v1/last-products')

if __name__ == '__main__':
    db.init_app(app)
    app.run(host='0.0.0.0', port=8080)
