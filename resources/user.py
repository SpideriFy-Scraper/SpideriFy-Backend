from sqlalchemy.sql.elements import Null
from flask_restful import Resource, reqparse
from flask import jsonify
from models.User import UserModel
from flask_jwt_extended import create_access_token


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


class SignUp(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True)
    parser.add_argument('firstname', type=str, required=True)
    parser.add_argument('lastname', type=str, required=True)
    parser.add_argument('email', type=str, required=True)
    parser.add_argument('password', type=str, required=True)

    def post(self):
        data = SignUp.parser.parse_args()
        username = str(data["username"])
        email = str(data["email"])
        phone_number = Null
        if "phone_number" in data:
            phone_number = str(data["phone_number"])

        user_check = UserModel.query.filter_by(username=username).one_or_none()
        if user_check:
            return jsonify("username has been registered! try another username"), 200

        email_check = UserModel.query.filter_by(email=email).one_or_none()
        if email_check:
            return jsonify("email has been registered! try another email"), 200

        UserModel(username, str(data["first_name"]), str(data["last_name"]),
                  email, str(data["password"]), phone_number, Null, Null)
