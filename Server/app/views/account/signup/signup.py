from flask import Blueprint, Response, abort, g, request
from flask_restful import Api

from app.models.account import UserModel as User
from app.views import api_blueprint, BaseResource

api = Api(api_blueprint)
api.prefix = ''


@api.resource('/check/id/<id>')
class CheckIDDuplicated(BaseResource):
    def get(self, id):
        query = User.select().where(User.id == id)
        if query.exists():
            return Response('', 406)
        else:
            return 200


@api.resource('/check/email/<email>')
class CheckEmailDuplicated(BaseResource):
    def get(self, email):
        query = User.select().where(User.email == email)
        if query.exists():
            return Response('', 406)
        else:
            return 200
