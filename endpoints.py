from flask_restful import Api
from flask import current_app

from resources.user import User, UserRegister, UserLogin, TokenRefresh, UserLogout

api = Api(current_app)
api.add_resource(User, "/user/<int:user_id>")
api.add_resource(UserRegister, "/register")
api.add_resource(UserLogin, "/login")
api.add_resource(TokenRefresh, "/refresh")
api.add_resource(UserLogout, "/logout")
