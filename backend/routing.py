from var import *
from app import *


app.add_url_rule("/meme", "all_files", all_files)
app.add_url_rule("/meme/<meme_id>", "all_files", all_files)

app.add_url_rule("/removed", "removed", removed)
app.add_url_rule("/new", "new", new)
app.add_url_rule("/moved", "moved", moved)


