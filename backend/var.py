from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

PATHDIR = "/media/randomguy90/cheny/"
DB_NAME = "sqlalchemy_example"
IP_FLASK = "127.0.0.1"
PORT_FLASK = 5000
PORT_IMGS = 5001

SINGLE_FILE_FETCH_COUNT = 50

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app, resources=r'/*')



