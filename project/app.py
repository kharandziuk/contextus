import json
from datetime import date
import tornado.escape
import tornado.ioloop
import tornado.web
import handlers

from tornado_routes import make_handlers

URL_PREFIX = 'api-v1'

handlers = make_handlers(
    URL_PREFIX,
    (r'/', include('handlers')),
)
application = tornado.web.Application(
    handlers
)
 
if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
