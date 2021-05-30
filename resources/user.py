from sqlalchemy.sql.elements import Null
from flask_restful import Resource, reqparse
from flask import jsonify
from models.User import UserModel
from pyisemail import is_email
from flask_jwt_extended import create_access_token, current_user


class Login(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username", type=str, required=True)
    parser.add_argument("password", type=str, required=True)

    def post(self):
        data = Login.parser.parse_args()
        username = str(data["username"])
        password = str(data["password"])
        if username == "" or password == "":
            return jsonify("username and password can not be empty"), 401

        user = UserModel.query.filter_by(username=username).one_or_none()
        if not user or not user.check_password(password):
            return jsonify("Wrong username or password"), 401

        # Notice that we are passing in the actual sqlalchemy user object here
        access_token = create_access_token(identity=user)
        return jsonify(access_token=access_token)


class Register(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username", type=str, required=True)
    parser.add_argument("firstname", type=str, required=True)
    parser.add_argument("lastname", type=str, required=True)
    parser.add_argument("email", type=str, required=True)
    parser.add_argument("password", type=str, required=True)  # Password Must Get Hashed

    def post(self):
        data = Register.parser.parse_args()
        username = str(data["username"])
        email = str(data["email"])
        firstname = str(data["firstname"])
        lastname = str(data["lastname"])
        passwoed = str(data["password"])

        detailed_result_with_dns = is_email(email, check_dns=True, diagnose=True)
        phone_number = None
        if "phone_number" in data:
            phone_number = str(data["phone_number"])
        user_check = UserModel.query.filter_by(username=username).one_or_none()
        if user_check:
            return (
                jsonify("username has been registered! try another username"),
                409,
            )  # Conflict
        email_check = UserModel.query.filter_by(email=email).one_or_none()
        if email_check:
            return (
                jsonify("email has been registered! try another email"),
                409,
            )  # Conflict
        UserModel(
            username,
            str(data["first_name"]),
            str(data["last_name"]),
            email,
            str(data["password"]),
            phone_number,
            True,
            False,
        )
