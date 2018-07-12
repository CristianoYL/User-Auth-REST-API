from flask_restful import Resource, request
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_refresh_token_required,
    jwt_optional,
    fresh_jwt_required,
    get_jwt_identity,
    jwt_required,
    get_raw_jwt,
)
from models.user import UserModel
from schemas.user import UserSchema
from blacklist import BLACKLIST

user_schema = UserSchema()


class UserRegister(Resource):
    @classmethod
    def post(cls):
        user = user_schema.load(request.get_json())

        if UserModel.find_by_username(user.username):
            return {"message": "A user with that username already exists."}, 400

        user.save_to_db()
        return {"message": "User created successfully."}, 201


class User(Resource):
    @classmethod
    @jwt_optional
    def get(cls, user_id: int):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {"message": "User not found."}, 404
        if get_jwt_identity():
            return {
                "id": user.id,
                "username": user.username,
                "password": user.password
                   }, 200
        return user_schema.dump(user), 200

    @classmethod
    @jwt_required
    def delete(cls, user_id: int):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {"message": "User not found."}, 404

        user.delete_from_db()
        return {"message": "User deleted."}, 200


class UserLogin(Resource):
    @classmethod
    def post(cls):
        user_data = user_schema.load(request.get_json())
        
        user = UserModel.find_by_username(user_data.username)

        if user and safe_str_cmp(user_data.password, user.password):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            return {"access_token": access_token, "refresh_token": refresh_token}, 200

        return {"message": "Invalid credentials!"}, 401


class UserLogout(Resource):
    @classmethod
    @jwt_required
    def post(cls):
        jti = get_raw_jwt()["jti"]  # jti is "JWT ID", a unique identifier for a JWT.
        user_id = get_jwt_identity()
        BLACKLIST.add(jti)
        return {"message": f"User <id={user_id}> successfully logged out."}, 200


class TokenRefresh(Resource):
    @classmethod
    @jwt_refresh_token_required
    def post(cls):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)
        return {"access_token": new_token}, 200


class UserUpdate(Resource):
    # TODO: revoke all tokens for this user

    @classmethod
    @fresh_jwt_required
    def put(cls, user_id):
        """
        update password
        """
        user = UserModel.find_by_id(user_id)
        if not user:
            return {"message": "User not found."}, 400

        data = user_schema.load(request.get_json())
        user.password = data.password
        user.save_to_db()

        return {"message": "User password updated."}, 200

