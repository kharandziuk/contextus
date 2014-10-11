import unittest
from app import application
from webtest import TestApp
from tornado.testing import LogTrapTestCase

import tornado.wsgi

import models, factories
from backend import db


class TestSequenceFunctions(LogTrapTestCase):
    def test_get(self):
        db.query(models.Post).delete()
        db.commit()
        post = factories.PostFactory()
        db.commit()
        assert post.body
        app = TestApp(tornado.wsgi.WSGIAdapter(application))
        resp = app.get('/posts')
        actual = resp.json
        self.assertItemsEqual(actual['posts'], [{'body': post.body}])
        self.assertEqual(resp.status_code, 200)

    def test_post(self):
        app = TestApp(tornado.wsgi.WSGIAdapter(application))
        resp = app.post('/posts', params={'body': 'some text'})
        self.assertEqual(resp.status_code, 200)

if __name__ == "__main__":
    unittest.main()
