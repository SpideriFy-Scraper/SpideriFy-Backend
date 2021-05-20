from flask_restful import Resource, reqparse
from models.Product import ProductModel
from models.User import UserModel
from common.db import db
from crawler.SpiderifyWrapper import SpiderifyWrapper
from flask import jsonify, Response, json

# ("/user/login/") - -> class Login - -> POST


class Login(Resource):
    def post(self):
        pass
