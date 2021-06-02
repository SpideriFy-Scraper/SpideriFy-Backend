from flask import jsonify
from flask_jwt_extended import create_access_token, current_user
from flask_restful import Resource, reqparse
from pyisemail import is_email
from sqlalchemy.sql.elements import Null
from models.User import UserModel


class UserLoginAPI(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username", type=str, required=True, help="This Field Is Username Of The User That Wants To Login")
    parser.add_argument("password", type=str, required=True, help="This Field Is Password Of The User That Wants To Login")

    @classmethod
    def post(cls):
        data = cls.parser.parse_args()
        if not (data["username"] or data["password"]):
            return jsonify({"message": "Username Or Password Can Not Be Empty"}), 401

        user = UserModel.query.filter_by(username=data["username"]).one_or_none()

        if user and user.check_password(data["password"]):
            access_token = create_access_token(identity=user.id)
            return jsonify(access_token=access_token), 200

        return jsonify({"message": "Invalid Credentials"}), 401



class UserRegisterAPI(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username", type=str, required=True, help="This Field Is Username Of The User That Wants To Register")
    parser.add_argument("password", type=str, required=True, help="This Field Is Password Of The User That Wants To Register")
    parser.add_argument("firstname", type=str, required=True)
    parser.add_argument("lastname", type=str, required=True)
    parser.add_argument("email", type=str, required=True)

    @classmethod
    def post(cls):
        data = cls.parser.parse_args()
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
