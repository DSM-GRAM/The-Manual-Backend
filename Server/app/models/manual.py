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

    user_name = CharField(
        null=False
    )
    
    user_email = CharField(
        null=False
    )
    #name이랑 email은 가져오는건데 어떻게 합니까?

    #관리자인지 아닌지 어떻게 알아야할지 모르겠씁니당

    #자기 앨범수랑 질문수랑 답변수는 어디서 ... 가져와요..?

    #최근활동은..?


class Album(BaseModel):

    title = CharField(
        null=False
    )
    # - 앨범의 제목

    # image =
    # - 사진


    # - (어디서 했는지) 위치

    # - (매뉴얼 DB에 있는 사람 중)함께한 사람 추가
