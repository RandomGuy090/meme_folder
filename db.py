import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()
 
class Memes(Base):
    __tablename__ = 'memes_table'
    id = Column(Integer, primary_key=True)
    filename = Column(String(250), nullable=False)
    path = Column(String(250), nullable=False)
    full_filename = Column(String(250), nullable=False)
    exists = Column(Boolean(), nullable=False)


 
class Tags(Base):
    __tablename__ = 'tag_table'
    id = Column(Integer, primary_key=True)
    tag_name = Column(String(250), nullable=False, unique=True)



class Map_tags(Base):
    __tablename__ = 'map_tags'
    id = Column(Integer, primary_key=True)
    # meme_id = Column(Integer, nullable=False)
    # tag_id = Column(Integer, nullable=False)

    meme_id = Column(Integer, ForeignKey("memes_table.id"))
    tag_id = Column(Integer, ForeignKey("tag_table.id"))

    meme = relationship("Memes")
    tag = relationship("Tags")



if "-c" in sys.argv or "--create" in sys.argv:
    engine = create_engine('sqlite:///sqlalchemy_example.db')
    Base.metadata.create_all(engine)



# SELECT filename, 
#     group_concat(tag_name,' ~ ') AS tags_for_this_object 
# FROM map_tags 
# JOIN memes_table ON meme_id = memes_table.id
# JOIN tag_table ON tag_id = tag_table.id
# GROUP BY filename
# ;


# SELECT filename, 
#     group_concat(tag_name,' ~ ') AS tags_for_this_object 
# FROM map_tags 
# JOIN memes_table ON meme_id = memes_table.id
# JOIN tag_table ON tag_id = tag_table.id
# WHERE tag_table.tag_name LIKE "kabaczek"
# GROUP BY filename
# ;