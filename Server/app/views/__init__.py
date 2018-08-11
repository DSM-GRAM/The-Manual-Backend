from flask import Blueprint, Response
from flask_restful import Resource
import json

api_blueprint = Blueprint('api', __name__)


class BaseResource(Resource):
    @classmethod
    def unicode_safe_json_dumps(cls, data, status_code=200):
        return Response(
            json.dumps(data, ensure_ascii=False),
            status_code,
            content_type='application/json; charset=utf8'
        )


def route(app):
    from app.views.account.auth import auth

    app.register_blueprint(api_blueprint)
