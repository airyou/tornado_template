# -*- coding: utf-8 -*-

import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import define, options

import os

#setting port number
define("port", default=10000, help="run on the given port", type=int)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("welcome to tornado")
        self.finish()


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', IndexHandler)
        ]
        template_path = os.path.join(os.path.dirname(__file__), "templates")
        static_path = os.path.join(os.path.dirname(__file__), "static")
        tornado.web.Application.__init__(
            self,
            handlers,
            debug=True,
            template_path=template_path,
            static_path=static_path,
            cookie_secret='development secret key',
        )


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()