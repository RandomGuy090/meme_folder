from flask import Flask, request, jsonify
from flask_marshmallow import Marshmallow 

from db import Memes, Map_tags, Tags
from checking import Check_existance
from meme import Memes
from database import Database
from var import *

import os

app = Flask(__name__)

ma = Marshmallow(app)

class All_memes(ma.Schema):
  class Meta:
    fields = ('id', 'filename', 'path', 'full_filename', 'exists', "shasum")

all_memes = All_memes(many=True)


class Checked_files(ma.Schema):
  class Meta:
    fields = ('id', 'filename', 'path', 'full_filename', 'exists', "shasum")

checked_files = Checked_files(many=True)


@app.route("/all_files", methods=["GET"])
def all_files():

	memes = Database(DB_NAME).list_all_memes(api=True).all()
	res = all_memes.dump(memes)
	return jsonify(res)

@app.route("/removed", methods=["GET"])
def removed():

	ex = Check_existance(db_name=DB_NAME)
	removed = ex.removed()
	print(removed)
	res = checked_files.dump(removed)
	return jsonify(res)

@app.route("/new", methods=["GET"])
def new():
	
	ex = Check_existance(db_name=DB_NAME)
	removed = ex.new()
	print(removed)
	res = checked_files.dump(removed)
	return jsonify(res)



if __name__ == '__main__':
  app.run(debug=True)