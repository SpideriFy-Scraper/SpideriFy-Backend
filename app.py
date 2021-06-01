from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restful import Api

from common.db import db
from models.User import UserModel
from resources.comment import CommentsList
from resources.product import LastProducts, NewProduct, Product, ProductsList
from resources.user import Login, Register

app = Flask(__name__)
jwt = JWTManager(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return UserModel.query.filter_by(id=identity).one_or_none()


if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
elif app.config["ENV"] == "development":
    app.config.from_object("config.DevelopmentConfig")
else:
    app.config.from_object("config.TestingConfig")

api = Api(app)

api.add_resource(NewProduct, "/api/v1/new-product")
api.add_resource(Register, "/api/v1/user/register")
api.add_resource(Login, "/api/v1/user/login")
api.add_resource(ProductsList, "/api/v1/products")
api.add_resource(Product, "/api/v1/product/<string:asin>")
api.add_resource(CommentsList, "/api/v1/product/<string:asin>/comments")
api.add_resource(LastProducts, "/api/v1/last-products")

if __name__ == "__main__":
    db.init_app(app)
    app.run(host="0.0.0.0", port=8080)
