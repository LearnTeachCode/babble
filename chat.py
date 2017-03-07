import tornado.web
import tornado.websocket


class ChatSocket(tornado.websocket.WebSocketHandler):
    def open(self):
        print("Socket Opened")
    
    def on_message(self, message):
        print(message)
        self.write_message(message)
    
    def on_close(self):
        print("Socket Closed")

class ChatHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('chat.html')
