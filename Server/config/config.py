import os
import socket


class Config:
    SERVICE_NAME = 'The_Manual'

    RUN_SETTING = {
        'threaded': True
    }

    MYSQL_SETTING = {
        'database': SERVICE_NAME,
        'username': os.getenv('MYSQL_USERNAME', 'root'),
        'password': os.getenv('MYSQL_PW', '')
    }
    # -> 일반적으로 데이터베이스 인스턴스는 다른 데에 분리하는 방식으로 구성해서,
    # ProductionConfig에서 원격(실제) 데이터베이스 설정을, DevConfig에서 로컬 데이터베이스 설정을 둬야 하지만
    # 우리의 경우에는 서버가 돌아가는 인스턴스에 데이터베이스가 딸려 있으니, 로컬 MySQL에 연결하는 설정을 여기서 global하게 관리함

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
