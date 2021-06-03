from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restful import Api

from common.db import db
from common.blocklist import BLOCKLIST
from models.User import UserModel
from resources.comment import CommentsList
from resources.product import LastProducts, NewProduct, Product, ProductsList
from resources.user import UserLoginAPI, UserRegisterAPI, User, UserLogoutAPI

app = Flask(__name__)
jwt = JWTManager(app)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

@jwt.additional_claims_loader
def add_claims_to_access_token(identity):
    if identity == 1:
        return {'is_admin': True}
    return {'is_admin': False}

@jwt.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_header, jwt_payload):
    jti = jwt_payload["jti"]
    return jti in BLOCKLIST

@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return UserModel.query.filter_by(id=identity).one_or_none()

@jwt.expired_token_loader
def expired_token_callback():
    return jsonify({
        'description': 'The token has been expired',
        'error': 'token_expired'
    }), 401

@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({
        'description': 'Signiture verification failed',
        'error': 'invalid_token'
    }), 401


@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({
        'description': 'Request does not cantain an access token',
        'error': 'authorization_required'
    }), 401

@jwt.revoked_token_loader
def revoked_token_callback():
    return jsonify({
        'description': 'The token hass been revoked',
        'error': 'token_revoked'
    }), 401

if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
elif app.config["ENV"] == "development":
    app.config.from_object("config.DevelopmentConfig")
else:
    app.config.from_object("config.TestingConfig")

api = Api(app)

api.add_resource(NewProduct, "/api/v1/new-product")
api.add_resource(UserRegisterAPI, "/api/v1/user/register")
api.add_resource(UserLoginAPI, "/api/v1/user/login")
api.add_resource(UserLogoutAPI, "/api/v1/user/logout")
api.add_resource(User, "/api/v1/user/<int:user_id>")
api.add_resource(ProductsList, "/api/v1/products")
api.add_resource(Product, "/api/v1/product/<string:asin>")
api.add_resource(CommentsList, "/api/v1/product/<string:asin>/comments")
api.add_resource(LastProducts, "/api/v1/last-products")

if __name__ == "__main__":
    db.init_app(app)
    app.run(host="0.0.0.0", port=8080)
