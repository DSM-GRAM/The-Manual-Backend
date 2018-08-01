from flask import Response
from flask_restful import Resource
import json


class BaseResource(Resource):
    @classmethod
    def unicode_safe_json_dumps(cls, data, status_code=200):
        return Response(
            json.dumps(data, ensure_ascii=False),
            status_code,
            content_type='application/json; charset=utf8'
        )


def route(app):
    from app.views.account import account

    app.register_blueprint(account.api.blueprint)
