# from app import app
from routing import app
from http_server import run_http_server
from threading import Thread
from app import *

if __name__ == '__main__':

  # flask_thread = Thread(target = app.run, kwargs={"debug":True, "host":"127.0.0.1", "port":12345}).start()
  http_thread = Thread(target = run_http_server).start()
  app.run(host=IP_FLASK, port=PORT_FLASK)

  # run_http_server()
  