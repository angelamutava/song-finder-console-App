from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import MultipleResultsFound
from prettytable import PrettyTable
import urllib2
import urllib
import json
import textwrap

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

# Declaring the static variables for configuration.
api_key = "5120626c22645c776a9a863c9b0859c4"
musix_match_url = "http://api.musixmatch.com/ws/1.1/"

# Returns a list of songs that match the criteria.
def song_find(query_string):
	full_url = musix_match_url + "track.search?q_track=" + urllib.quote(query_string) + "&apikey=" + api_key + "&json"
	try:
		request_stmt = urllib2.Request(full_url)
        # Can pass timeout time to the urlopen method
		data = urllib2.urlopen(request_stmt)
		the_page = data.read()
		lyrics = json.loads(the_page.decode("utf-8"))
		data.close()
		# To get the tracks with the given query string from the json string
		list_tracks = lyrics['message']['body']['track_list']
		get_len = len(list_tracks)
		list_of_all_tracks = []
		count = 0
		while count <= get_len - 1:
			list_specific_track = []
			# get the track_details
			get_track_id = list_tracks[count]['track']['track_id']
			get_song_name = list_tracks[count]['track']['track_name']
			get_song_album_name = list_tracks[count]['track']['album_name']
			get_song_artist_name = list_tracks[count]['track']['artist_name']
			count += 1
			list_specific_track.insert(0, get_track_id)
			list_specific_track.insert(1, get_song_name)
			list_specific_track.insert(2, get_song_album_name)
			list_specific_track.insert(3, get_song_artist_name)
			list_of_all_tracks.append(list_specific_track)
	except urllib2.URLError as e:
		print e.reason

song_find('casting crown')		


# View song lyrics based on its id. Should be optimized by checking 
# if theres a local copy before checking online
def song_view(track_id):

# To view a song you need to check if it is in the database before looking for it online.
	
	try:
		find_song = session.query(SongFinder).filter(SongFinder.song_id == track_id).one()
		print 'Getting data from Database'
		print find_song.song_id
		dedented_text = textwrap.dedent(find_song.song_lyrics).strip()
		print textwrap.fill(dedented_text, width=20)
	except MultipleResultsFound:
		find_song = session.query(SongFinder).filter(SongFinder.song_id == track_id).all()
		for item in find_song:
			print item.song_id
			dedented_text = textwrap.dedent(item.song_lyrics).strip()
			print textwrap.fill(dedented_text, width=20)
	except NoResultFound:
		print "Getting data from the API"
		full_url = musix_match_url + "track.lyrics.get?track_id=" + track_id + "&apikey=" + api_key + "&json"
		# can pass data and headers to te Request method.

		
		try:
			request_stmt = urllib2.Request(full_url)
        	# can pass timeout time to the urlopen method
			data = urllib2.urlopen(request_stmt)
			the_page = data.read()
			lyrics = json.loads(the_page.decode("utf-8"))
			data.close()
			get_len = len(lyrics["message"]["body"])
			if get_len == 0:
				print "lyrics not found in musixmatch"
			else:
				dedented_text = textwrap.dedent(lyrics["message"]["body"]["lyrics"]["lyrics_body"]).strip()
				print textwrap.fill(dedented_text, width=20)
		except urllib2.URLError as e:
			print e.reason
song_view('15953433')

# Clear entire local song database.
def song_clear(input_value):

	print "Are you sure you want to clear the database?"
 	user_input = input("Enter yes/YES or no/NO")
 	if input_value == "yes" or input_value == 'YES':
 		try:
 			deleted_rows = db.session.query(SongFinder).delete()
 			db.session.commit()
 			print "Database cleared successfully."
 		except:
 			db.session.rollback()
 	else:
 		sys.exit()
 		

def song_save(track_id):

	# This method saves the song to the database
	full_url = musix_match_url + "track.lyrics.get?track_id=" + track_id + "&apikey=" + api_key + "&json"
    # can pass data and headers to the Request method.
	request_stmt = urllib2.Request(full_url)
    # can pass timeout time to the urlopen method
	try:
		data = urllib2.urlopen(request_stmt)
		the_page = data.read()
		lyrics = json.loads(the_page.decode("utf-8"))
		data.close()
		get_len = len(lyrics["message"]["body"])
		if get_len == 0:
			print "Song not found in musixmatch"
		else:
			lyrics_content = lyrics["message"]["body"]["lyrics"]["lyrics_body"]
			song_found = SongFinder(track_id, lyrics_content)
			session.add(song_found)
			session.commit()
	except urllib2.URLError as e:
		print e.reason

song_save('15953433')
