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



res = os.listdir(PATHDIR)
ret = list()

ex = Check_existance(db_name=DB_NAME)

ls = ex.check_replacement()

new_files =ex.new()
removed = ex.removed()

if ls:
	for elem in ls:
		# print(f"{elem.get('old').filename} --->> {elem.get('new').filename}")
		print(f"{elem.meme_new.filename} --->> {elem.meme_old.filename}")

for new in new_files:
	print(f"new --------> {new.filename}")
for old in removed:
	print(f"removed  <------ {old.filename}")



# meme = Meme("/media/randomguy90/cheny/spurdoWerhmacht.png", db_name=DB_NAME)

# print(meme.meme_tags())
# meme.add_tag(tag_name="spurdo")
# meme.remove_tag(tag_name="spurdo")
# print(meme.meme_tags())
 
# # for elem in x:
# # 	print(elem, x[elem])

sys.exit(0)


for elem in res:
	# ret.append(os.path.realpath(elem))
	x = Meme(elem, db_name=DB_NAME)
	x.insert_to_db()
	

	# a = Memes(filename=x.filename, path=x.path, full_filename=x.full_filename)
	# session.add(a)
	# session.commit()


# print(ret)