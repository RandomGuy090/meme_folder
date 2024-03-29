from var import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, func, literal_column
from db import Memes, Tags, Map_tags
import hashlib, os



class Meme_queries(object):
	def get_by_name_like(self, name, api=False):
		session = self.check_session()

		search = "%{}%".format(name)
		qr = session.query(Memes).filter(Memes.filename.like(search))

		if api:
			return qr

		names = list()
		for elem in qr:
			names.append(elem.full_filename)

		return names	


	def list_all_memes(self, api=False, meme_id=None):
		session = self.check_session()
		
		# qr = session.query(Memes).order_by(Memes.full_filename)
		('id', 'filename', 'path', 'full_filename', 'exists', "shasum")
		qr = session.query(Map_tags.meme_id, 
			Memes.filename,
			Memes.path,
			Memes.full_filename,
			Memes.exists,
			Memes.shasum,
			func.group_concat(Tags.tag_name.op(' ')(literal_column(",'~'")))).join(Memes ,Memes.id==Map_tags.meme_id).join(Tags ,Tags.id==Map_tags.tag_id).group_by(Memes.id)

		if meme_id:
			qr = qr.filter(Map_tags.meme_id==int(meme_id))

		if api:
			return qr
		names = list()
		for elem in qr:
			names.append(elem.full_filename)

		return names	

	def get_by_hash(self, hashed, api=False):
		session = self.check_session()
		qr = session.query(Memes).order_by(Memes.full_filename).filter(Memes.shasum == hashed).all()
		if api:
			return qr
		names = list()
		for elem in qr:
			names.append(elem.full_filename)

		return names


class Tags_queries(object):
	def list_all_tags(self, api=False):
		session = self.check_session()
		qr = session.query(Tags).order_by(Tags.id).all()

		if api:
			return qr
		return None

	def list_by_tags(self, api=False, tag_id=None):
		session = self.check_session()
		if tag_id == None:
			return False

		try:
			tag_id = int(tag_id)
		except ValueError:
			tag_id = str(tag_id)

		if isinstance(tag_id, int):
			# qr = session.query(Map_tags.meme_id, 
			# 	Memes.filename,
			# 	Memes.path,
			# 	Memes.full_filename,
			# 	Memes.exists,
			# 	Memes.shasum,
			# 	func.group_concat(Tags.tag_name.op(' ')(literal_column(",'~'")))).join(Memes ,Memes.id==Map_tags.meme_id).join(Tags ,Tags.id==Map_tags.tag_id).group_by(Memes.id)\
			# .join(Memes ,Memes.id==Map_tags.meme_id)\
			# .join(Tags ,Tags.id==Map_tags.tag_id)\
			# .filter(Tags.id == tag_id)\
			# .group_by(Memes.id)
			qr = session.query(Map_tags.meme_id, 
			Memes.filename,
			Memes.path,
			Memes.full_filename,
			Memes.exists,
			Memes.shasum,
			func.group_concat(Tags.tag_name.op(' ')(literal_column(",'~'")))).join(Memes ,Memes.id==Map_tags.meme_id).join(Tags ,Tags.id==Map_tags.tag_id).group_by(Memes.id)\
			.filter(Tags.id == tag_id)\
			.group_by(Memes.id)

		elif isinstance(tag_id, str):
			# qr = session.query(Map_tags.meme_id, 
			# 	Memes.filename,
			# 	Memes.path,
			# 	Memes.full_filename,
			# 	Memes.exists,
			# 	Memes.shasum,
			# 	func.group_concat(Tags.tag_name.op(' ')(literal_column(",'~'")))).join(Memes ,Memes.id==Map_tags.meme_id).join(Tags ,Tags.id==Map_tags.tag_id).group_by(Memes.id)\
			# .join(Memes ,Memes.id==Map_tags.meme_id)\
			# .join(Tags ,Tags.id==Map_tags.tag_id)\
			# .filter(Tags.tag_name == tag_id)\
			# .group_by(Memes.id)

			qr = session.query(Map_tags.meme_id, 
			Memes.filename,
			Memes.path,
			Memes.full_filename,
			Memes.exists,
			Memes.shasum,
			func.group_concat(Tags.tag_name.op(' ')(literal_column(",'~'")))).join(Memes ,Memes.id==Map_tags.meme_id).join(Tags ,Tags.id==Map_tags.tag_id).group_by(Memes.id)\
			.filter(Tags.tag_name == tag_id)\
			.group_by(Memes.id)

		return qr.all()

	def create_tag(self, tag_name, api=False):
		session = self.check_session()
		try:
			qr = Tags(tag_name=tag_name)
			session.add(qr)
			session.commit()
			session.close()
			return True
		except Exception as e:
			return False
			pass

	def remove_tag(self, tag_name, api=False):
		session = self.check_session()
		d = session.query(Tags).filter(Tags.tag_name==tag_name).delete()
		session.commit()
		return True


class Database(Tags_queries, Meme_queries):
	def __init__(self, db_name):
		self.BUF_SIZE = 65536 


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

	def get_shasum(self, file=None):
		sha1 = hashlib.sha1()

		file = self.full_filename if file==None else file
		
		if not os.path.exists(file):
			return ""

		if os.path.isdir(file):
			return file

		with open(file, 'rb') as f:
			while True:
				data = f.read(self.BUF_SIZE)
				if not data:
					break
				sha1.update(data)
		
		out = sha1.hexdigest()
		return out
