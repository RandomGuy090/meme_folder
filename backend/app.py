
from db import Memes, Map_tags, Tags, New_files_table
from checking import Check_existance
from meme import Meme
from database import Database

import os, json
from serialize import *
from routing import app

def search():
	search = request.args.get("search")

	memes = Database(DB_NAME).get_by_name_like(api=True, name=search)
	memes = memes.all()
	res = new_files.dump(memes)
	return jsonify(res)

@cross_origin()
def all_files(meme_id=None):
	
	if meme_id:
		memes = Database(DB_NAME).list_all_memes(api=True, meme_id=meme_id)
		memes = memes.all()
	else:
		memes = Database(DB_NAME).list_all_memes(api=True)
		page = request.args.get("page")
		memes = memes.all()
		
		if page:
			page = int(page)
			memes = memes[page*SINGLE_FILE_FETCH_COUNT:(page+1)*SINGLE_FILE_FETCH_COUNT]
			

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
	if request.method == "GET":
		tags = Database(DB_NAME).list_all_tags(api=True)
		res = all_tags_ser.dump(tags)
		return jsonify(res)

	elif request.method == "POST":
		data = request.data.decode("utf-8")
		data = json.loads(data)
		tag = Database(DB_NAME).create_tag(api=True, tag_name=data.get("tag_name"))
		if tag:
			tags = Database(DB_NAME).list_all_tags(api=True)
			res = all_tags_ser.dump(tags)
			return jsonify(res)
		else:
			return jsonify({"error": f"cannot add tag: {data.get('tag_name')}"})
	elif request.method == "DELETE":
		data = request.data.decode("utf-8")
		data = json.loads(data)
		tag = Database(DB_NAME).remove_tag(api=True, tag_name=data.get("tag_name"))
		if tag:
			tags = Database(DB_NAME).list_all_tags(api=True)
			res = all_tags_ser.dump(tags)
			return jsonify(res)
		else:
			return jsonify({"error": f"cannot remove tag: {data.get('tag_name')}"})



def get_by_tags(tag_id):
	tags = Database(DB_NAME).list_by_tags(api=True, tag_id=tag_id)
	res = all_memes.dump(tags)
	return jsonify(res)


def add_tag_to_file(meme_id, tag_id):
	memes = Database(DB_NAME).list_all_memes(api=True, meme_id=int(meme_id))
	res = all_memes.dump(memes)[0]

	meme_obj = Meme(res.get("full_filename"), db_name=DB_NAME)

	if request.method == "POST":
		try:
			meme_obj.add_tag(tag_id=int(tag_id))
		except:
			return jsonify({"status": "501", "error": "no such tag"})

	if request.method == "DELETE":
		try:
			meme_obj.remove_tag(tag_id=int(tag_id))
		except:
			return jsonify({"status": "501", "error": "no such tag"})

	memes = Database(DB_NAME).list_all_memes(api=True, meme_id=int(meme_id))
	res = all_memes.dump(memes)[0]
	return jsonify(res)
	# return jsonify({"status": 501})


if __name__ == '__main__':
  app.run(debug=True)