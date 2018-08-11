from flask import Blueprint, Response, abort, g, request
from flask_restful import Api

from app.models.account import UserModel
from app.views import api_blueprint, BaseResource

api = Api(api_blueprint)
api.prefix = ''


@api.resource('/check/id/<id>')
class CheckIDDuplicated(BaseResource):
    def get(self, id):
        """
        ID 중복체크
        """


@api.resource('/check/email/<email>')
class CheckEmailDuplicated(BaseResource):
    def get(self, email):
        """
        이메일 중복체크
        """
