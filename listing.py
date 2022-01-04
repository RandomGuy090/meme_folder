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


Database(DB_NAME).create_tag("directory")
Database(DB_NAME).create_tag("link")
Database(DB_NAME).create_tag("file")


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
