from peewee import *

from app.models import BaseModel


class Manual(BaseModel):

    title = CharField(
        null=False
    )
    # 메뉴얼의 제목

    # how to use ListField in peewee?
    # 같이 하는 멤버


class Main(BaseModel):

    # profile_image =

    # background_image =


class Album(BaseModel):

    title = CharField(
        null=False
    )
    # - 앨범의 제목

    # image =
    # - 사진


    # - (어디서 했는지) 위치

    # - (매뉴얼 DB에 있는 사람 중)함께한 사람 추가
