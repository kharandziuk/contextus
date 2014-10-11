import tornado.escape
import tornado.ioloop
from tornado import web
import os

from tornado_routes import make_handlers, include

ROOT = os.getcwd()

URL_PREFIX = ''

handlers = make_handlers(
    URL_PREFIX,
    (r'api-v1/', include('handlers')),
)
application = web.Application(
    handlers
)

reverse_url = application.reverse_url

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
