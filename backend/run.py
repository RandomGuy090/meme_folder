# from app import app
from routing import app
from http_server import run_http_server

if __name__ == '__main__':
  # run_http_server()
  app.run(debug=True)