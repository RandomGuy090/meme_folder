import os, sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from db import Memes, Tags, Map_tags

DB_NAME = "sqlalchemy_example"

engine = create_engine(f'sqlite:///{DB_NAME}.db')

Session = sessionmaker(bind=engine)
session = Session()


def create_tag(tag_name):
	try:
		qr = Tags(tag_name=tag_name)
		session.add(qr)
		session.commit()
		session.close()
	except Exception as e:
		# print(e)
		pass

create_tag("directory")
create_tag("link")
create_tag("file")


PATHDIR = "/path/to/dir"
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
		self.tags = []
		self.meme_object = None

		if db_name != None:
			self.db_name = db_name
		else:
			self.db_name = "memes"
		
		super().__init__(self.db_name)

				
		self.set_engine(self.db_name)
		
		
		

	def get_tags(self):
		print(self.engine.table_names)
		session = self.check_session()
		# qr = session.query(Map_tags).join(Tags, id==Map_tags.tag_id).join(Memes,id==Map_tags.meme_id).all()
		qr = session.query(Tags).all()
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
			print(tag)
			print(tag.tag_name)
			print(session)
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

		

class Tag(object):
	def __init__(self, name=None):

		self.tag_name = name



class Check_existance(Database):
	def __init__(self, db_name):
		super().__init__(db_name)
		self.set_engine(db_name)
		self.new_files = []
		self.removed_files = []

		
		self.list_all()
		diff = self.get_diff(self.listed, self.listed_db)
		if len(diff) == 0 :

			print("no difference")
		else:
			print("diff")
			for elem in diff:
				if os.path.exists(elem):
					self.new_files.append(elem)
				else:
					self.removed_files.append(elem)




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

	def new(self):
		return self.new_files

	def removed(self):
		return self.removed_files







res = os.listdir(PATHDIR)
ret = list()
ex = Check_existance(db_name=DB_NAME)
new_files = ex.new()
for elem in new_files:
	print(f"New File: {elem}")

removed = ex.removed()
for elem in removed:
	print(f"Removed File: {elem}")





for elem in res:
	# ret.append(os.path.realpath(elem))
	x = Meme(elem, db_name=DB_NAME)
	x.insert_to_db()
	print(x.filename)

	# a = Memes(filename=x.filename, path=x.path, full_filename=x.full_filename)
	# session.add(a)
	# session.commit()


print(session.add)
# print(ret)