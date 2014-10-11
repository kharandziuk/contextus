from sqlalchemy import Column, Integer, String

from model import Model


class User(Model):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column('username', String)
