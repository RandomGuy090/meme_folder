
from db import Memes, Map_tags, Tags, New_files_table
from checking import Check_existance
from meme import Memes
from database import Database

import os, json
from serialize import *
from routing import app


def all_files(meme_id=None):

	if meme_id:
		memes = Database(DB_NAME).list_all_memes(api=True, meme_id=meme_id)
	else:
		memes = Database(DB_NAME).list_all_memes(api=True)

	memes = memes.all()
	res = all_memes.dump(memes)

	return jsonify(res)


def removed():

	ex = Check_existance(db_name=DB_NAME)
	removed = ex.removed()
	res = removed_files.dump(removed)
	return jsonify(res)


def new():
	
	ex = Check_existance(db_name=DB_NAME)
	removed = ex.new()
	res = new_files.dump(removed)
	return jsonify(res)

def moved():
	
	ex = Check_existance(db_name=DB_NAME)
	moved = ex.check_replacement()
	res = moved_files.dump(moved)
	return jsonify(res)

def all_tags():

	tags = Database(DB_NAME).list_all_tags(api=True)
	res = all_tags_ser.dump(tags)
	return jsonify(res)

def get_by_tags(tag_id):
	print(tag_id)
	
	tags = Database(DB_NAME).list_by_tags(api=True, tag_id=tag_id)

	print(tags)
	res = new_files.dump(tags)
	return jsonify(res)

if __name__ == '__main__':
  app.run(debug=True)