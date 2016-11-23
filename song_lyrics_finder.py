from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import MultipleResultsFound
import urllib.request

from model import SongFinder, Base

engine = create_engine('sqlite:///songs.db', echo=True)

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Declaring the static variables.
api_key = "5120626c22645c776a9a863c9b0859c4"
musix_match_url = "http://api.musixmatch.com/ws/1.1/"

# Returns a list of songs that match the criteria.
def song_find():
	pass

# View song lyrics based on its id. Should be optimized by checking 
# if theres a local copy before checking online
def song_view(track_id):

# To view a song you need to check it in the database before looking for it online
	
	try:
		find_song = session.query(SongFinder).filter(song_id == track_id).one()
		print 'Getting data from Database'
		print find_song.song_id
		print find_song.song_lyrics

	except NoResultFound:
		print "Getting data from the API"
		full_url = musix_match_url + "track.lyrics.get?track_id=" + track_id + "&apikey=" + api_key + "&json"
		# can pass data and headers to te Request method.
		request_stmt = urllib.request.Request(full_url)
        	# can pass timeout time to the urlopen method
		try:
			data = urllib.request.urlopen(request_stmt)
			the_page = data.read()
			lyrics = json.loads(the_page.decode("utf-8"))
			get_len = len(lyrics["message"]["body"])
			if get_len == 0:
				print "lyrics not founff in musixmatch"
			else:
				print lyrics["message"]["body"]["lyrics"]["lyrics_body"]
		except urllib.error.URLError as e:
			print e.reason
song_view('15953433')        	





	

# Store song details and lyrics locally..
# def song_save():
	# pass

# Clear entire local song database.	
# def song_clear():
#	pass	
