import os, sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from db import Memes, Tags, Mapping
DB_NAME = "sqlalchemy_example"

engine = create_engine(f'sqlite:///{DB_NAME}.db')

Session = sessionmaker(bind=engine)
session = Session()


def create_tag(tag_name):
	try:
		qr = Tags(tag_name=tag_name)
		session.add(qr)
		session.commit()
	except Exception as e:
		# print(e)
		pass

create_tag("directory")
create_tag("link")
create_tag("file")

PATHDIR = "/media/randomguy90/cheny/"
# PATHDIR = "/home/randomguy90/"

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



class Meme(Database):
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
		
		super().__init__(self.db_name)

				
		self.set_engine(self.db_name)
		self.insert_to_db()
		
		# self.printout()
		if self.is_link:
			self.add_tag("link")
		elif self.is_dir:
			self.add_tag("directory")
		else:
			self.add_tag("file")



	def printout(self):
		print(self.full_filename)


	def insert_to_db(self, db=None):
		session = self.check_session()

		qr = Memes(filename=self.filename, path=self.path, full_filename=self.full_filename, exists=True)
		session.add(qr)
		session.flush()
		session.refresh(qr)
		self.meme_id = qr.id
		# print(self.meme_id)
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



class Check_existance(Database):
	def __init__(self, db_name):
		super().__init__(db_name)
		self.set_engine(db_name)
		
		self.list_all()
		diff = self.get_diff(self.listed, self.listed_db)
		if len(diff) == 0 :
			print("no difference")
		else:
			print("diff")
			print(diff)
			for elem in diff:
				if os.path.exists(elem):
					print(f"NEW {elem}")
				else:
					print(f"REMOVED {elem}")



	def get_diff(self, l1, l2):
		x = list(set(l1) - set(l2)) + list(set(l2) - set(l1))
		return  x

	def list_all(self):
		tmp = os.listdir(PATHDIR)
		def x(x):
			return f"{PATHDIR}{x}"

		listed = list(map(x, tmp))
		self.listed = sorted(listed)
		self.listed_db = self.list_all_memes()









res = os.listdir(PATHDIR)
ret = list()
Check_existance(db_name=DB_NAME)

sys.exit(0)

for elem in res:
	# ret.append(os.path.realpath(elem))
	x = Meme(elem, db_name=DB_NAME)
	print(x.filename)
	if "anon" in x.filename:
		create_tag("kabaczek")

		x.add_tag(tag_name="kabaczek")
	# a = Memes(filename=x.filename, path=x.path, full_filename=x.full_filename)
	# session.add(a)
	# session.commit()


print(session.add)
# print(ret)