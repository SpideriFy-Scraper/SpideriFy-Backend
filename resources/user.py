from flask import jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_raw_jwt
from flask_restful import Resource, reqparse
from pyisemail import is_email
from models.User import UserModel
from common.blacklist import BLACKLIST


class User(Resource):
    @classmethod
    def get(cls, user_id):
        user = UserModel.query.filter_by(id=user_id).one_or_none()
        if not user:
            return jsonify({"message": "User Not Found"}), 404
        return jsonify(user.json()), 200
    @classmethod
    def delete(cls, user_id):
        user = UserModel.query.filter_by(id=user_id).one_or_none()
        if not user:
            return jsonify({"message": "User Not Found"}), 404
        user.delete_from_db()
        return jsonify({"message": "User Deleted"}), 200

class UserRegisterAPI(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username", type=str, required=True, help="This Field Is Username Of The User That Wants To Register")
    parser.add_argument("password", type=str, required=True, help="This Field Is Password Of The User That Wants To Register")
    parser.add_argument("firstname", type=str, required=True, help="This Field Is First_name Of The User That Wants To Register")
    parser.add_argument("lastname", type=str, required=True, help="This Field Is Last_name Of The User That Wants To Register")
    parser.add_argument("email", type=str, required=True, help="This Field Is Email Of The User That Wants To Register")
    parser.add_argument("phone_number", type=str, required=False, help="This Field Is Phone Of The User That Wants To Register")

    @classmethod
    def post(cls):
        data = cls.parser.parse_args()
        username = data["username"]
        email = data["email"]
        firstname = data["firstname"]
        lastname = data["lastname"]
        password = data["password"]

        if "phone_number" in data:
            phone_number = data["phone_number"]

        user = UserModel.query.filter_by(username=username).one_or_none()
        if user:
            return jsonify({"message": "Username has been registered! try another username"}), 400

        email_check = UserModel.query.filter_by(email=email).one_or_none()
        if email_check:
            return jsonify({"message": "Email has been registered! try another email"}), 400

        detailed_result_with_dns = is_email(email, check_dns=True, diagnose=True)
        if not detailed_result_with_dns:
            return jsonify({"message": "Invalid Email"}), 401

        new_user = UserModel(
            username=username,
            first_name=firstname,
            last_name=lastname,
            email=email,
            password=password,
            phone_number=phone_number,
            is_active=True,
            is_admin=False,
        )
        new_user.save_to_db()
        return jsonify({"message": "User Created Successfully"}), 201


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


class UserLogoutAPI(Resource):
    @jwt_required
    def post(self):
        jti = get_raw_jwt()['jti']
        BLACKLIST.add(jti)
        return jsonify({"message": "Successfully Logged Out"}), 200


