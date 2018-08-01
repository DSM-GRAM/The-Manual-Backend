from peewee import *

from app.models import BaseModel


class Manual(BaseModel):
    pass
    # 메뉴얼의 제목
    # 같이 하는 멤버


class Main(BaseModel):
    pass
    # 프사 배사


class Album(BaseModel):
    pass
    # - 앨범의 제목
    # - 사진
    # - (어디서 했는지) 위치

    # - (매뉴얼 DB에 있는 사람 중)함께한 사람 추가
