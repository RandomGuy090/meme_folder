import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from db import Memes, Tags, Mapping

engine = create_engine('sqlite:///sqlalchemy_example.db')

Session = sessionmaker(bind=engine)
session = Session()


def create_tag(tag_name):
	try:
		qr = Tags(tag_name=tag_name)
		session.add(qr)
		session.commit()
	except Exception as e:
		print(e)

create_tag("directory")
create_tag("link")
create_tag("file")

# PATHDIR = "/media/randomguy90/cheny/webmy/"
PATHDIR = "/home/randomguy90/"

class Meme(object):
	def __init__(self, name, db_name=None):
		self.filename = name
		self.path = PATHDIR
		self.full_filename = f"{PATHDIR}{self.filename}" if PATHDIR.endswith("/") else f"{PATHDIR}/{self.filename}"

		self.is_dir = os.path.isdir(self.full_filename)
		self.is_link = os.path.islink(self.full_filename)

		if db_name != None:
			self.db_name = db_name
		else:
			self.db_name = "memes"
				
		self.set_engine(self.db_name)
		self.insert_to_db()
		
		# self.printout()
		if self.is_dir:
			self.add_tag("directory")
		elif self.is_link:
			self.add_tag("link")
		else:
			self.add_tag("file")



	def printout(self):
		print(self.full_filename)

	def set_engine(self, db_name):
		self.engine = create_engine(f'sqlite:///{db_name}.db')

	def check_session(self):
		if self.engine:
			Session = sessionmaker(bind=self.engine)
			session = Session()
			return session
		else:
			raise Exception("engine not binded")

	def insert_to_db(self, db=None):
		session = self.check_session()

		qr = Memes(filename=self.filename, path=self.path, full_filename=self.full_filename)
		session.add(qr)
		session.flush()
		session.refresh(qr)
		self.meme_id = qr.id
		# print(self.meme_id)

		session.commit()

	def add_new_tag(self, tag_name=None):
		session = self.check_session()

		if tag_name == None:
			raise Exception("tag_name not defined") 

		qr = Tags(tag_name=tag_name)
		session.add(qr)


		session.commit()

	def add_tag(self, tag_name):
		session = self.check_session()
		try:
			q = session.query(Tags)
			q = q.filter(Tags.tag_name==tag_name)
			tag = q.one()
		except:
			raise Exception("no such tag ")

		qr = Mapping(meme_id=self.meme_id, tag_id=tag.id)
		session.add(qr)
		session.commit()


		

class Tag(object):
	def __init__(self, name=None):
		self.tag_name = name



res = os.listdir(PATHDIR)
ret = list()

for elem in res:
	# ret.append(os.path.realpath(elem))
	x = Meme(elem, db_name="sqlalchemy_example")
	# a = Memes(filename=x.filename, path=x.path, full_filename=x.full_filename)
	# session.add(a)
	# session.commit()


print(session.add)
# print(ret)