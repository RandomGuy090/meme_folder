
from db import Memes, Map_tags, Tags, New_files_table
from checking import Check_existance
from meme import Memes
from database import Database

import os, json

from serialize import *
from var import *


@app.route("/meme", methods=["GET"])
@app.route("/meme/<meme_id>", methods=["GET"])
def all_files(meme_id=None):

	if meme_id:
		memes = Database(DB_NAME).list_all_memes(api=True, meme_id=meme_id)
	else:
		memes = Database(DB_NAME).list_all_memes(api=True)


	memes = memes.all()
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