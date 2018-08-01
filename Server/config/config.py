import os
import socket


class Config:
    SERVICE_NAME = 'The_Manual'

    RUN_SETTING = {
        'threaded': True
    }

    MYSQL_SETTING = {
        'database': SERVICE_NAME
    }

    SECRET_KEY = os.getenv('SECRET_KEY', '85c145a16bd6f6e1f3e104ca78c6a102')


class DevConfig(Config):
    HOST = 'localhost'
    PORT = 5000
    DEBUG = True

    RUN_SETTING = dict(Config.RUN_SETTING, **{
        'host': HOST,
        'port': PORT,
        'debug': DEBUG
    })


class ProductionConfig(Config):
    HOST = socket.gethostbyname(socket.gethostname())
    PORT = 80
    DEBUG = False

    RUN_SETTING = dict(Config.RUN_SETTING, **{
        'host': HOST,
        'port': PORT,
        'debug': DEBUG
    })
