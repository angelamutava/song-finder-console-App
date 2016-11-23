from sqlalchemy import create_engine
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class SongFinder(Base):
	__tablename__ = 'lyrics'
	# Here we define columns for the table lyrics
    # Each column is also a normal Python instance attribute.
	id = Column(Integer, primary_key=True)
	song_id = Column(String(200), nullable=False)
	song_lyrics = Column(String(700), nullable=False)

	def __init__(self, song_id, song_lyrics):
		self.song_id = song_id
		self.song_lyrics = song_lyrics

# Create an engine that stores data in the local directory's
# songs.db file.
engine = create_engine('sqlite:///songs.db', echo=True)

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)


