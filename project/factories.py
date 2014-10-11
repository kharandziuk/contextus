from backend import db
import models
import factory
from factory.alchemy import SQLAlchemyModelFactory as Factory


class PostFactory(Factory):
    class Meta:
        model = models.Post
        sqlalchemy_session = db

    body = 'text'
