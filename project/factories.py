from backend import db
import models
import factory
from factory.alchemy import SQLAlchemyModelFactory as Factory


class PostFactory(Factory):
    class Meta:
        model = models.Post
        sqlalchemy_session = db

    body = factory.Sequence(lambda x: 'post {}'.format(x))


class UserFactory(Factory):
    class Meta:
        model = models.User
        sqlalchemy_session = db

    username = factory.Sequence(lambda x: 'username{}'.format(x))
