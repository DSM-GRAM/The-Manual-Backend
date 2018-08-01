from flask import Flask
from peewee import MySQLDatabase

from app.views import route
from config.config import Config

db = MySQLDatabase(Config.MYSQL_SETTING['database'])


def create_app(*config_cls):
    app = Flask(__name__)

    for config in config_cls:
        app.config.from_object(config)

    route(app)
    db.connect()

    return app
