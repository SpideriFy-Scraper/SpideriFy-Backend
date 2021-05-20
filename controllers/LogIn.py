from flask_jwt_extended import create_access_token
from flask_restful import Resource, reqparse
from flask import jsonify
from models.User import UserModel


class LogIn(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True)
    parser.add_argument('password', type=str, required=True)

    def post(self):
        data = LogIn.parser.parse_args()
        username = str(data["username"])
        password = str(data["password"])
        if username == '' or password == '':
            return jsonify("username and password can not be empty"), 401

        user = UserModel.query.filter_by(username=username).one_or_none()
        if not user or not user.check_password(password):
            return jsonify("Wrong username or password"), 401

        # Notice that we are passing in the actual sqlalchemy user object here
        access_token = create_access_token(identity=user)
        return jsonify(access_token=access_token)


