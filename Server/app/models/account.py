from peewee import *

from app.models import BaseModel


class UserModel(BaseModel):
    """
    사용자 model
    """

    id = CharField(
        primary_key=True
    )

    pw_hashed = CharField(
        null=True
    )

    email = CharField(
        null=True
    )

    email_certified = BooleanField(
        default=False
    )

    name = CharField(
        null=False
    )
