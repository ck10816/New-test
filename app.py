from src.helper import print_hello_world

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("Hello, Tornado!")

def make_app():
	return tornado.web.Application([(r"/", MainHandler)])

if __name__ == "__main__":
	

	app = make_app()
	app.listen(8888)
	print_hello_world()
	tornado.ioloop.IOLoop.current().start()