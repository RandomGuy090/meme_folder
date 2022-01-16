
from flask_marshmallow import Marshmallow 
import os, json
from var import * 
from db import *


class Serialise_data(object):

	def get_fields(self, object):
		l = dir(object)
		
		ret = []


		for elem in l:
			if not elem.startswith("__") and\
			not elem.startswith("_") and\
			not  elem.endswith("__"):
				ret.append(elem)

		return ret

	def serialise_tags(self, qr, key="id"):
		ret = dict()
		for map, tag, meme in qr: 

			try:
				ret[meme.id]["tags"].append(tag.tag_name)
			except KeyError:
				ret[meme.id] = {}
				ret[meme.id]["tags"] = [tag.tag_name]

			ret[meme.id]["filename"] = meme.filename
			ret[meme.id]["path"] = meme.path
			ret[meme.id]["full_filename"] = meme.full_filename
			ret[meme.id]["exists"] = meme.exists

		return ret
			
			


ma = Marshmallow(app)


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


class Moved_files(ma.Schema):
	class Meta:
		model = New_files_table
		fields = ( "meme_new", "meme_old")
	

	meme_new = ma.Nested(New_files)
	meme_old = ma.Nested(New_files)

moved_files = Moved_files(many=True)


class All_memes():

	class Meta:
		# model = Memes
		strict = True
		fields = ('id', 'filename', 'path', 'full_filename', 'exists', "shasum", "tags")

	def __init__(self,many=False):
		self.obj = None
		self.ret = list()

	def dump(self, obj):
		self.obj = obj
		return self.serialize()
	
	def serialize(self):
		for elem in self.obj:
			x = dict()
			for col in self.Meta.fields:
				val = self.get_values(element=elem, index=self.Meta.fields.index(col), separator="~")
				x[col] = val

			self.ret.append(x)
		return self.parse_json()
		
	def parse_json(self):
		return self.ret
		# return json.dumps(self.ret)

	def get_values(self, element=None, index=None, separator=""):
		column = self.Meta.fields[index]
		if column == "tags":
			return element[index].rsplit(separator)
		return element[index]


all_memes = All_memes(many=True)