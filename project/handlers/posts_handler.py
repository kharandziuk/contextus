import models, serializers
from base_handler import BaseHandler


@route('/posts', name='posts')
class PostHandler(BaseHandler):
    def get(self):
        db = self.backend.get_session()
        posts = db.query(models.Post).all()
        self.write({
            'posts': serializers.PostSerializer(posts, many=True).data,
            'status': 'ok'
        })
        db.close()

    def post(self):
        db = self.backend.get_session()
        post = models.Post(body="text")#**self.request.body_arguments)
        serializer = serializers.PostSerializer(post)
        if not serializer.is_valid():
            self.write({'status': 'ok'})
        db.add(post)
        db.commit()
        self.write({'status': 'ok'})
        db.close()

