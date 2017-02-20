import tornado.web
import tornado.websocket


class ChatSocket(tornado.websocket.WebSocketHandler):
    def open(self):
        pass
    
    def on_message(self, message):
        pass
    
    def write_message(self, message):
        pass
    
    def on_close(self):
        pass

class ChatHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('chat.html')
