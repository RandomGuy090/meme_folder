from var import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from db import Memes, Tags, Map_tags
import hashlib, os


class Database(object):
	def __init__(self, db_name):
		self.BUF_SIZE = 65536 

		self.sha1 = hashlib.sha1()

		self.set_engine(db_name)

	def set_engine(self, db_name):
		self.engine = create_engine(f'sqlite:///{db_name}.db')

	def check_session(self):
		if self.engine:
			Session = sessionmaker(bind=self.engine)
			session = Session()
			return session
		else:
			raise Exception("engine not binded")

	def list_all_memes(self):
		session = self.check_session()
		qr = session.query(Memes).order_by(Memes.full_filename)
		names = list()
		for elem in qr:
			names.append(elem.full_filename)

		return names

	def create_tag(self, tag_name):
		session = self.check_session()
		try:
			qr = Tags(tag_name=tag_name)
			session.add(qr)
			session.commit()
			session.close()
		except Exception as e:
			# print(e)
			pass

	def remove_tag(self, tag_name):
		session = self.check_session()
		d = session.query(Tags).filter(Tags.tag_name==tag_name).delete()
		session.commit()


	def get_by_hash(self, hashed):
		session = self.check_session()
		qr = session.query(Memes).order_by(Memes.full_filename).filter(Memes.shasum == hashed).all()
		
		names = list()
		for elem in qr:
			names.append(elem.full_filename)

		return names


	def get_shasum(self, file=None):
		file = self.full_filename if file==None else file
		if os.path.isdir(file):
			return ""

		with open(file, 'rb') as f:
			while True:
				data = f.read(self.BUF_SIZE)
				if not data:
					break
				self.sha1.update(data)
		
		out = self.sha1.hexdigest()
		return out



