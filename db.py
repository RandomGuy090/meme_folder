import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
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

 
class Tags(Base):
    __tablename__ = 'tag_table'
    id = Column(Integer, primary_key=True)
    tag_name = Column(String(250), nullable=False, unique=True)

class Mapping(Base):
    __tablename__ = 'mapping'
    id = Column(Integer, primary_key=True)
    meme_id = Column(Integer, nullable=False)
    tag_id = Column(Integer, nullable=False)



if "-c" in sys.argv or "--create" in sys.argv:
    engine = create_engine('sqlite:///sqlalchemy_example.db')
    Base.metadata.create_all(engine)



# SELECT filename, 
#     group_concat(tag_name,' ~ ') AS tags_for_this_object 
# FROM mapping 
# JOIN memes_table ON meme_id = memes_table.id
# JOIN tag_table ON tag_id = tag_table.id
# GROUP BY filename
# ;