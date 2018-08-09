from flask import Blueprint, Response, abort, request
from flask_restful import Api
from flask_jwt_extended import create_access_token, create_refresh_token
from werkzeug.security import generate_password_hash, check_password_hash

from app.views import BaseResource
from app.models.account import UserModel

api = Api(Blueprint(__name__, __name__))
api.prefix = '/user'


@api.resource('/signup')
class Signup(BaseResource):
    def post(self):
        payload = request.json

        id = payload['id']
        pw = payload['pw']
        email = payload['email']
        name = payload['name']

        pw_hashed = generate_password_hash(pw)

        if UserModel.select().where(id=id):
            abort(409)

        UserModel.insert(id=id, pw_hashed=pw_hashed, email=email, name=name).execute()

        return Response('success signup'), 201


@api.resource('/login')
class Login(BaseResource):
    def post(self):
        """
        로그인
        """
        payload = request.json

        id = payload['id']
        pw = payload['pw']

        users = UserModel.select().where(UserModel.id == id)

        user = users[0]

        if not user:
            abort(401)

        if not check_password_hash(user.pw_hashed, pw):
            abort(401)

        return {
                'access_token': create_access_token(identity=id),
                'refresh_token': create_refresh_token(identity=id)
        }

