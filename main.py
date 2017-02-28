import tornado.ioloop
import tornado.web
import os.path

class MainHandler(tornado.web.RequestHandler):
  def get(self):
    self.render("index.html")

def make_app():
  return tornado.web.Application(
    [
      (r"/", MainHandler),
    ],
    template_path = os.path.join(os.path.dirname(__file__), "templates"),
    static_path = os.path.join(os.path.dirname(__file__), "static")
  )

if __name__ == "__main__":
  app = make_app()
  app.listen(8888)
  tornado.ioloop.IOLoop.current().start()


