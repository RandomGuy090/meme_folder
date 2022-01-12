import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine, UniqueConstraint
 
Base = declarative_base()
 
class Memes(Base):
    __tablename__ = 'memes_table'
    id = Column(Integer, primary_key=True)
    filename = Column(String(250), nullable=False)
    path = Column(String(250), nullable=False)
    full_filename = Column(String(250), nullable=False)
    exists = Column(Boolean(), nullable=False)
    shasum = Column(String(50), nullable=False)


 
class Tags(Base):
    __tablename__ = 'tag_table'
    id = Column(Integer, primary_key=True)
    tag_name = Column(String(250), nullable=False, unique=True)




class Map_tags(Base):
    __tablename__ = 'map_tags'
    __table_args__ = (
        UniqueConstraint('meme_id', 'tag_id'),
        )
    
    id = Column(Integer, primary_key=True)
    # meme_id = Column(Integer, nullable=False)
    # tag_id = Column(Integer, nullable=False)

    meme_id = Column(Integer, ForeignKey("memes_table.id",onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    tag_id = Column(Integer, ForeignKey("tag_table.id", onupdate="CASCADE", ondelete="CASCADE"), nullable=False)

    meme = relationship("Memes")
    tag = relationship("Tags")

class New_files_table(Base):
    __tablename__ = "new_files_table"
    id = Column(Integer, primary_key=True)


    meme_new = Column(Integer, ForeignKey("memes_table.id",onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    meme_old = Column(Integer, ForeignKey("memes_table.id",onupdate="CASCADE", ondelete="CASCADE"), nullable=False)

    # meme_new = relationship("Memes")
    # meme_old = relationship("Memes")





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


# SELECT meme_id, filename, 
#     group_concat(tag_name,' ~ ') AS tags_for_this_object 
# FROM map_tags 
# JOIN memes_table ON meme_id = memes_table.id
# JOIN tag_table ON tag_id = tag_table.id
# WHERE   map_tags.meme_id LIKE 784
# GROUP BY meme_id
# ;

