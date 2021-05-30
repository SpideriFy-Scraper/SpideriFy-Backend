from flask import Response, json, jsonify
from flask_jwt_extended import jwt_required
from flask_restful import Resource, reqparse

from common.db import db
from models.Product import ProductModel
from models.User import UserModel


# ("/product/<string:asin>/comments")--> class CommentsList - -> GET
class CommentsList(Resource):
    def get(self):
        pass
