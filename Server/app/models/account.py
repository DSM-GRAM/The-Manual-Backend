from peewee import *

from app.models import BaseModel


class UserModel(BaseModel):
    id = CharField(
        primary_key=True
    )

    pw_hashed = CharField(
        null=False
    )

    email = CharField(
        null=False
    )

    email_auth = BooleanField(
        default=False
    )

    name = CharField(
        null=False
    )

    friend = IntegerField(
        default=0
    )

    # more