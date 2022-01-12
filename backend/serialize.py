

class Serialise_data(object):

	def get_fields(self, object):
		l = dir(object)
		
		ret = []


		for elem in l:
			if not elem.startswith("__") and\
			not elem.startswith("_") and\
			not  elem.endswith("__"):
				ret.append(elem)

		return ret

	def serialise_tags(self, qr, key="id"):
		ret = dict()
		for map, tag, meme in qr: 

			try:
				ret[meme.id]["tags"].append(tag.tag_name)
			except KeyError:
				ret[meme.id] = {}
				ret[meme.id]["tags"] = [tag.tag_name]

			ret[meme.id]["filename"] = meme.filename
			ret[meme.id]["path"] = meme.path
			ret[meme.id]["full_filename"] = meme.full_filename
			ret[meme.id]["exists"] = meme.exists

		return ret
			
			


