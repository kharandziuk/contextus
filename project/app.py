import json
from datetime import date
import tornado.escape
import tornado.ioloop
import tornado.web
import handlers

from tornado_routes import make_handlers, include

URL_PREFIX = ''

handlers = make_handlers(
    URL_PREFIX,
    (r'api-v1/', include('handlers')),
)
application = tornado.web.Application(
    handlers
)

reverse_url = application.reverse_url

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
