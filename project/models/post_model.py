from sqlalchemy import Column, Integer, String, DateTime, Boolean

from model import Model

class Post(Model):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    body = Column('body', String)

