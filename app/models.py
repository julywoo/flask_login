#coding:utf-8

import datetime
from sqlalchemy import Column,INT,String,DateTime,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship
from database import Base

#user table mapping

class User(Base):
    __tablename__='users'
    user_no=Column(INT,primary_key=True)
    user_name=Column(String(45),unique=False)
    user_id=Column(String(45),unique=True,nullable=False)
    user_pw=Column(String(45),nullable=False,unique=False)
    user_gender=Column(INT)
    user_img=Column(String(100))

    def __init__(self,user_name=user_name,user_pw=user_pw,user_id=user_id,
                 user_gender=user_gender,user_img=user_img):

        self.user_name=user_name
        self.user_id=user_id
        self.user_pw=user_pw
        self.user_gender=user_gender
        self.user_img=user_img

