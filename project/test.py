import unittest
from app import application
from webtest import TestApp
from tornado.testing import LogTrapTestCase

import tornado.wsgi

import models, factories
from backend import db
from app import reverse_url


class TestSequenceFunctions(LogTrapTestCase):
    def test_get(self):
        db.query(models.Post).delete()
        db.commit()
        post = factories.PostFactory()
        db.commit()
        app = TestApp(tornado.wsgi.WSGIAdapter(application))
        resp = app.get(reverse_url('posts'))
        actual = resp.json
        self.assertItemsEqual(actual['posts'], [{'body': post.body}])
        self.assertEqual(resp.status_code, 200)

    def test_post(self):
        app = TestApp(tornado.wsgi.WSGIAdapter(application))
        resp = app.post(reverse_url('posts'), params={'body': 'some text'})
        self.assertEqual(resp.status_code, 200)

if __name__ == "__main__":
    unittest.main()
