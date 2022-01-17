from flask import Flask, request, jsonify

PATHDIR = "/media/randomguy90/cheny/"
DB_NAME = "sqlalchemy_example"
app = Flask(__name__)
app.url_map.strict_slashes = False
