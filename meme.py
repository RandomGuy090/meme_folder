from database import  Database
from var import *
from serialize import Serialise_data
import os
from db import Memes, Tags, Map_tags


class Meme(Database, Serialise_data):
	def __init__(self, name, db_name=None):
		self.filename = name
		self.path = PATHDIR
		self.full_filename = f"{PATHDIR}{self.filename}" if PATHDIR.endswith("/") else f"{PATHDIR}/{self.filename}"

		self.is_dir = os.path.isdir(self.full_filename)
		self.is_link = os.path.islink(self.full_filename)
		self.tags = []
		self.meme_object = None

		if db_name != None:
			self.db_name = db_name
		else:
			self.db_name = "memes"
		
		Database.__init__(self, self.db_name)

				
		self.set_engine(self.db_name)
		
		
		

	def get_tags(self):
		# print(self.engine.table_names)
		session = self.check_session()
		
		qr = session.query(Map_tags, Tags, Memes).join(Tags).join(Memes).all()
		# qr = qr.group_by(Memes.id)

		ret = dict()
		fields = self.get_fields(Map_tags)

		for map, tag, meme in qr: 

			try:
				ret[meme.id]["tags"].append(tag.tag_name)
			except KeyError:
				ret[meme.id] = {}
				ret[meme.id]["tags"] = [tag.tag_name]
			ret[meme.id]["filename"] = meme.filename
			

		return ret


		# # qr = session.query(Tags).all()

		# print(qr)
		return qr
	def printout(self):
		print(self.full_filename)

	def type_flag(self):
		# self.printout()
		if self.is_link:
			self.add_tag("link")
		elif self.is_dir:
			self.add_tag("directory")
		else:
			self.add_tag("file")


	def insert_to_db(self, db=None):
		session = self.check_session()

		qr = Memes(filename=self.filename, path=self.path, full_filename=self.full_filename, exists=True)
		self.meme_object = qr
		session.add(qr)
		session.flush()
		session.refresh(qr)
		self.meme_id = qr.id
		# print(self.meme_id)
		session.commit()
		session.close()

		self.type_flag()


	def add_tag(self, tag_name):
		session = self.check_session()
		try:
			q = session.query(Tags)
			q = q.filter(Tags.tag_name==tag_name)
			tag = q.one()
			session.expunge(tag)
			session.close()
		except:
			raise Exception("no such tag ")

		if self.meme_object == None:
			# session = self.check_session()
			self.meme_object = session.query(Memes).filter(id==self.meme_id).one()
			session.flush()
			session.close()

		# session = self.check_session()
		# print(session)
		session.add(tag)
		session.add(self.meme_object)

		qr = Map_tags(meme=self.meme_object, tag=tag)


		session.add(qr)
		session.commit()
		session.close()

		