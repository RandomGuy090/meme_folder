from var import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from db import Memes, Tags, Map_tags

class Database(object):
	def __init__(self, db_name):
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


