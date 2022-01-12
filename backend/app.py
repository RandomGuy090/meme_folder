from flask import Flask, request, jsonify
from flask_marshmallow import Marshmallow 

from db import Memes, Map_tags, Tags, New_files_table
from checking import Check_existance
from meme import Memes
from database import Database
from var import *

import os

app = Flask(__name__)

ma = Marshmallow(app)

class All_memes(ma.Schema):
	class Meta:
		model = Memes
		fields = ('id', 'filename', 'path', 'full_filename', 'exists', "shasum")

all_memes = All_memes(many=True)


class Removed_files(ma.Schema):
	class Meta:
  		model = Memes
  		fields = ('id', 'filename', 'path', 'full_filename', 'exists', "shasum")

removed_files = Removed_files(many=True)

class New_files(ma.Schema):
	class Meta:
		model = Memes
		fields = ('id', 'filename', 'path', 'full_filename', 'exists', "shasum")

new_files = New_files(many=True)


# class Moved_files(ma.Schema):
#   class Meta:
#     fields = ('id', 'filename', 'path', 'full_filename', 'exists', "shasum")

# moved_files = Moved_files(many=True)



class Moved_files(ma.Schema):
	class Meta:
		model = New_files_table
		fields = ( "meme_new", "meme_old")
	

	meme_new = ma.Nested(New_files)
	meme_old = ma.Nested(New_files)

moved_files = Moved_files(many=True)


@app.route("/all_files", methods=["GET"])
def all_files():

	memes = Database(DB_NAME).list_all_memes(api=True).all()
	res = all_memes.dump(memes)
	return jsonify(res)


@app.route("/removed", methods=["GET"])
def removed():

	ex = Check_existance(db_name=DB_NAME)
	removed = ex.removed()
	res = removed_files.dump(removed)
	return jsonify(res)


@app.route("/new", methods=["GET"])
def new():
	
	ex = Check_existance(db_name=DB_NAME)
	removed = ex.new()
	res = new_files.dump(removed)
	return jsonify(res)

@app.route("/moved", methods=["GET"])
def moved():
	
	ex = Check_existance(db_name=DB_NAME)
	moved = ex.check_replacement()
	res = moved_files.dump(moved)
	return jsonify(res)




if __name__ == '__main__':
  app.run(debug=True)