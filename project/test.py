import unittest
from app import application
from webtest import TestApp
from tornado.testing import LogTrapTestCase

import tornado.wsgi

import models
import factories
from backend import db
from app import reverse_url


class PostsTestCase(LogTrapTestCase):

    def test_url(self):
        self.assertEqual(
            '/api-v1/users',
            reverse_url('users'),
        )

    def test_get(self):
        db.query(models.Post).delete()
        db.commit()
        post = factories.PostFactory()
        db.commit()
        app = TestApp(tornado.wsgi.WSGIAdapter(application))
        resp = app.get(reverse_url('posts'))
        actual = resp.json
        self.assertItemsEqual(actual['results'], [{'body': post.body}])
        self.assertEqual(resp.status_code, 200)

    def test_post(self):
        app = TestApp(tornado.wsgi.WSGIAdapter(application))
        resp = app.post(reverse_url('posts'), params={'body': 'some text'})
        self.assertEqual(resp.status_code, 200)


class UsersTestCase(LogTrapTestCase):

    def test_url(self):
        self.assertEqual(
            '/api-v1/users',
            reverse_url('users'),
        )

    def test_get(self):
        db.query(models.User).delete()
        db.commit()
        user = factories.UserFactory()
        db.commit()
        app = TestApp(tornado.wsgi.WSGIAdapter(application))
        resp = app.get(reverse_url('users'))
        actual = resp.json
        self.assertItemsEqual(actual['results'], [{'id': user.id, 'username': user.username}])
        self.assertEqual(resp.status_code, 200)

    # def test_post(self):
    #    app = TestApp(tornado.wsgi.WSGIAdapter(application))
    #    resp = app.post(reverse_url('posts'), params={'body': 'some text'})
    #    self.assertEqual(resp.status_code, 200)


if __name__ == "__main__":
    unittest.main()
