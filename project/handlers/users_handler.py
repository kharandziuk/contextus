from tornado_routes import route

import models
import serializers
from base_handler import BaseHandler


@route('/users', name='users')
class UsersHandler(BaseHandler):
    def get(self):
        db = self.backend.get_session()
        users = db.query(models.User).all()
        self.write({
            'results': serializers.UserSerializer(users, many=True).data,
            'status': 'ok'
        })
        db.close()
