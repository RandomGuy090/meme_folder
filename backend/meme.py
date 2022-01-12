from serialize import Serialise_data
from db import Memes, Tags, Map_tags
from database import  Database
from var import *
import os, time


class Meme(Database, Serialise_data):
	def __init__(self, name, db_name=None):
		


		self.filename = os.path.basename(name)

		self.path = PATHDIR
		self.full_filename = f"{PATHDIR}/{self.filename}"

		self.full_filename = self.full_filename.replace("//", "/")

		if self.full_filename.startswith(self.path*2):
			self.full_filename = self.full_filename[len(self.path):]


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


	def get_meme_data(self):
		# print(self.engine.table_names)
		session = self.check_session()
		qr = session.query(Map_tags, Tags, Memes).filter(Memes.full_filename==self.full_filename).join(Tags).join(Memes)
		# qr = session.query(Map_tags, Tags, Memes).join(Tags).join(Memes)
		qr = qr.all()
		ret = dict()
		
		# fields = self.get_fields(Map_tags)

		ret = self.serialise_tags(qr=qr)
		return ret

	def meme_tags(self):
		info = self.get_meme_data()
		index = list(info)[0]
		info = info[index].get("tags")
		return info

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

	def get_meme_id(self):
		session = self.check_session()
		# session = self.check_session()
		self.meme_object = session.query(Memes).filter(Memes.full_filename==self.full_filename).one()
		session.flush()
		session.close()



	def insert_to_db(self, db=None):
		shasum = self.get_shasum()
		

		session = self.check_session()

		qr = Memes(filename=self.filename, path=self.path, 
			full_filename=self.full_filename, exists=True,
			shasum = shasum)
		self.meme_object = qr
		session.add(qr)
		session.flush()
		session.refresh(qr)
		self.meme_id = qr.id
		# print(self.meme_id)
		session.commit()
		session.close()

		self.type_flag()

	def remove_meme(self):
		print(f"remove: {self.full_filename}")
		session = self.check_session()

		qr = session.query(Memes).filter(Memes.full_filename == self.full_filename)
		qr = qr.delete()
		session.add(qr)
		session.flush()
		session.refresh(qr)
		# print(self.meme_id)
		session.commit()
		session.close()




	def add_tag(self, tag_name):
		self.create_tag(tag_name)
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
			self.get_meme_id()
			
		# session = self.check_session()
		# print(session)
		session.add(tag)
		session.add(self.meme_object)

		qr = Map_tags(meme=self.meme_object, tag=tag)
		
		session.add(qr)
		try:
			session.commit()
		except:
			pass

		session.close()

		
	def remove_tag(self, tag_name):
		session = self.check_session()
		qr = session.query(Map_tags, Tags, Memes).filter(Memes.full_filename==self.full_filename).join(Tags).join(Memes)
		# qr = session.query(Map_tags, Tags, Memes).join(Tags).join(Memes)
		qr = qr.all()
		for map, tags, meme in qr:
			if tags.tag_name == tag_name:
				# tags.delete()
				d = session.query(Map_tags).filter(Map_tags.tag_id==tags.id).delete()



		session.commit()
		session.close()

	

		