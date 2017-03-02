#!/usr/bin/env python3
import tornado.ioloop
import tornado.web
import os.path

from chat import ChatSocket, ChatHandler

class MainHandler(tornado.web.RequestHandler):
  def get(self):
    self.render("index.html")

def make_app():
  return tornado.web.Application(
    [
      (r"/$", MainHandler),
      (r'/chat$', ChatHandler),
      (r'/chatsock$', ChatSocket)
    ],
    template_path = os.path.join(os.path.dirname(__file__), "templates"),
    static_path = os.path.join(os.path.dirname(__file__), "static")
  )

if __name__ == "__main__":
  app = make_app()
  app.listen(8000)
  tornado.ioloop.IOLoop.current().start()
