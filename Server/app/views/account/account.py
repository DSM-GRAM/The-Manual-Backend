from flask import Blueprint
from flask_restful import Api

from app.views import BaseResource

api = Api(Blueprint(__name__, __name__))


@api.resource('/user/login')
class Login(BaseResource):
    def post(self):
        """
        로그인
        """

        return 'hi'
