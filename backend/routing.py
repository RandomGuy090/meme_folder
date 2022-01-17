from var import *
from app import *


app.add_url_rule("/meme/<meme_id>/add_tag/<tag_id>","add_tag_to_file", add_tag_to_file )
app.add_url_rule("/meme/<meme_id>", "all_files", all_files)
app.add_url_rule("/meme", "all_files", all_files)


app.add_url_rule("/removed", "removed", removed)
app.add_url_rule("/new", "new", new)
app.add_url_rule("/moved", "moved", moved)
app.add_url_rule("/tags", "tags", all_tags)
app.add_url_rule("/tags/<tag_id>", "get_by_tags", get_by_tags)



