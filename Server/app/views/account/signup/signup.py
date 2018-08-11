from flask import Blueprint, Response, abort, g, request
from flask_restful import Api
from werkzeug.security import generate_password_hash

from app.models.account import UserModel as User
from app.views import api_blueprint, BaseResource

api = Api(api_blueprint)
api.prefix = ''


@api.resource('/check/id/<id>')
class CheckIDDuplicated(BaseResource):
    def get(self, id):
        query = User.select().where(User.id == id)

        return Response('', 409 if query.exists() else 200)


@api.resource('/check/email/<email>')
class CheckEmailDuplicated(BaseResource):
    def get(self, email):
        query = User.select().where(User.email == email)

        return Response('', 409 if query.exists() else 200)


@api.resource('/signup')
class Signup(BaseResource):
    def post(self):
        payload = request.json

        id = payload['id']
        pw = payload['pw']
        email = payload['email']
        name = payload['name']

        pw_hashed = generate_password_hash(pw)

        if User.select().where(id=id) or User.select().where(email=email):
            abort(409)

        User.insert(id=id, pw_hashed=pw_hashed, email=email, name=name).execute()

        return Response('', 201)

