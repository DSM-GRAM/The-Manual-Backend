from flask import Response, abort, request
from flask_restful import Api
from flask_jwt_extended import create_access_token, create_refresh_token
from werkzeug.security import check_password_hash

from app.views import BaseResource, api_blueprint
from app.models.account import UserModel as User

api = Api(api_blueprint)
api.prefix = ''


@api.resource('/login')
class Login(BaseResource):
    def post(self):
        """
        로그인
        """
        payload = request.json

        id = payload['id']
        pw = payload['pw']

        users = User.select().where(User.id == id)

        user = users[0]

        if not user:
            abort(401)

        if not check_password_hash(user.pw_hashed, pw):
            abort(401)

        return {
                'access_token': create_access_token(identity=id),
                'refresh_token': create_refresh_token(identity=id)
        }

