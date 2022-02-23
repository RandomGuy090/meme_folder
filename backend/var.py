from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

PATHDIR = "/media/randomguy90/cheny/"
DB_NAME = "sqlalchemy_example"
PORT = 5000

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app, resources=r'/*')



