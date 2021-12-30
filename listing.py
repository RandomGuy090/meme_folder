import os, sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from db import Memes, Tags, Map_tags

from var import *
from checking import Check_existance
from database import Database
from meme import Meme

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

# PATHDIR = "/home/randomguy90/"



class Tag(object):
	def __init__(self, name=None):

		self.tag_name = name









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