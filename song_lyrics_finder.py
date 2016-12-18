from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import MultipleResultsFound
from prettytable import PrettyTable
import urllib2
import urllib
import json
import textwrap
import click
from model import SongFinder, Base
from tqdm import tqdm

engine = create_engine('sqlite:///songs.db')

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database

session = DBSession()

# Declaring the static variables for configuration.
api_key = "5120626c22645c776a9a863c9b0859c4"
musix_match_url = "http://api.musixmatch.com/ws/1.1/"

# Returns a list of songs that match the criteria.
def song_find(query_string):
	"""
	This is a function that returns list of songs based on the query passed
	"""
	full_url = musix_match_url + "track.search?q_track=" + query_string + "&apikey=" + api_key + "&json"
	try:
		request_stmt = urllib2.Request(full_url)
		data = urllib2.urlopen(request_stmt)
		the_page = data.read()
		lyrics = json.loads(the_page.decode("utf-8"))
		data.close()
		list_tracks = lyrics['message']['body']['track_list']
		list_of_all_songs = []
		track_table = PrettyTable(['Track Id', 'Track Name', 'Artist Name'])
		for tracks in list_tracks:
			song_details = []
			get_track_id = tracks['track']['track_id']
			get_song_name = tracks['track']['track_name']
			get_song_artist_name = tracks['track']['artist_name']
			song_details.insert(0, get_track_id)
			song_details.insert(1, get_song_name)
			song_details.insert(2, get_song_artist_name)
			list_of_all_songs.append(song_details)
			track_table.add_row([get_track_id, get_song_name, get_song_artist_name])
		print track_table

	except urllib2.URLError as e:
		print 'No internet connection, connect and try again.'

		

def song_view(track_id):
	"""This function returns the song lyrics"""
	try:
		int(track_id)
		try:
			find_song = session.query(SongFinder).filter(SongFinder.song_id == track_id).one()
			print 'Getting lyrics from Database'
			print click.style(find_song.song_lyrics, fg='yellow')
		except MultipleResultsFound:
			find_song = session.query(SongFinder).filter(SongFinder.song_id == track_id).all()
			for item in find_song:
				print click.style(item.song_lyrics, fg='yellow')
		except NoResultFound:
			full_url = musix_match_url + "track.lyrics.get?track_id=" + track_id + "&apikey=" + api_key + "&json"
			try:
				request_stmt = urllib2.Request(full_url)
				data = urllib2.urlopen(request_stmt)
				the_page = data.read()
				lyrics = json.loads(the_page.decode("utf-8"))
				data.close()
				print click.style(lyrics["message"]["body"]["lyrics"]["lyrics_body"], fg="yellow")
			except urllib2.URLError as e:
				print 'No internet connection, connect and try again'

	except ValueError:
		print 'Track id should be a number, please try again'


def song_clear():
	"""This function clears the entire database."""
	try:
		deleted_rows = session.query(SongFinder).delete()
		session.commit()
		print "Database cleared successfully."
 	except:
 		session.rollback()
 	


def song_clear_single_song(track_id):
	"""This function clears a single song from the database."""	
	try:
		song_deleted = session.query(SongFinder).filter(SongFinder.song_id == track_id).delete()
		session.commit()
		print "Song deleted successfully"
	except:
		session.rollback()

def song_save(track_id):
	"""This function saves the song to the database."""
	try:
		int(track_id)
		full_url = musix_match_url + "track.lyrics.get?track_id=" + track_id + "&apikey=" + api_key + "&json"
		request_stmt = urllib2.Request(full_url)
		try:
			data = urllib2.urlopen(request_stmt)
			the_page = data.read()
			lyrics = json.loads(the_page.decode("utf-8"))
			data.close()
			lyrics_content = lyrics["message"]["body"]["lyrics"]["lyrics_body"]
			song_found = SongFinder(track_id, lyrics_content)
			session.add(song_found)
			session.commit()
			print "Song saved successfully."
		except urllib2.URLError as e:
			print 'No internet connection, connect and try again.'
	except ValueError:
		print 'Track id should be a number, please try again.'


def song_album(album_id):
    """This function returns the album of a particular song based on that album id"""
    try:
    	int(album_id)
    	full_url = musix_match_url + "album.get?album_id=" + album_id + "&apikey=" + api_key + "&json"
    	request_stmt = urllib2.Request(full_url)
    	try:
    		data = urllib2.urlopen(request_stmt)
    		the_page = data.read()
    		album = json.loads(the_page.decode("utf-8"))
    		data.close()
    		album_table = PrettyTable(['Album Id', 'Album Name', 'Artist Name'])
    		get_album_id = album["message"]["body"]["album"]["album_id"]
    		get_album_name = album["message"]["body"]["album"]["album_name"]
    		get_artist_name = album["message"]["body"]["album"]["artist_name"]
    		album_table.add_row([get_album_id, get_album_name, get_artist_name])
    	except urllib2.URLError as e:
    		print 'No internet connection, connect and try again.'
	except ValueError:
		print 'Track id should be a number, please try again.'

	def search_artist(artist_name):
		full_url = musix_match_url + "artist.search?q_artist=" + query_name + "&apikey=" + api_key + "&json"
		try:
			request_stmt = urllib2.Request(full_url)
		 	data = urllib2.urlopen(request_stmt)
			the_page = data.read()
			artists = json.loads(the_page.decode("utf-8"))
			data.close()
			list_artists = lyrics['message']['body']['artist_list']
			list_of_all_artists = []
			track_table = PrettyTable(['Artist Id', 'Artist Name', 'Artist Country'])
			for artists in list_artists:
				artist_details = []
				get_artist_id = artists['artist']['artist_id']
				get_artist_name = artists['artist']['artist_name']
				get_artist_country = artists['artist']['artist_country']
				song_details.insert(0, get_artist_id)
				song_details.insert(1, get_artist_name)
				song_details.insert(2, get_artist_country)
				list_of_all_songs.append(song_details)
				track_table.add_row([get_artist_id, get_artist_name, get_artist_country])
			print track_table
		except urllib2.URLError as e:
			print 'No internet connection, connect and try again.'