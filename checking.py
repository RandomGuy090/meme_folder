from database import Database
import os
from var import *


class Check_existance(Database):
	def __init__(self, db_name):
		Database.__init__(self, db_name)
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

	def check_replacement(self):
		for elem in self.new_files:
			hashed = self.get_shasum(elem)
			l = self.get_by_hash(hashed)
			for old in l:
				return {"old":old, 
						"new": elem}

