from peewee import Model

from app import db


class BaseModel(Model):
    # Model 클래스마다 내부에 Meta 클래스를 가지지 않아도 되도록
    class Meta:
        database = db
