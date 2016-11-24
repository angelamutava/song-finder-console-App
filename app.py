"""DJ WEKA NGOMA
 This applicat
Usage:
	song_find <query>
	song_view <track_id>
	song_clear<>
	song_clear_single_song<track_id>
	song_save<track_id>
"""
import cmd
from docopt import docopt, DocoptExit
from song_lyrics_finder import *

def docopt_cmd(func):
	"""
	Decorator definition for the app.
	"""
	def fn(self, arg):
		try:
			opt = docopt(fn.__doc__, arg)
		except DocoptExit as e:
			msg = "Invalid command! See help."

			print(msg)
			print(e)
			return

		except SystemExit:
			return

		return func(self, opt)

	fn.__name__ = func.__name__
	fn.__doc__ = func.__doc__
	fn.__dict__.update(func.__dict__)

return fn

class LyricsFinder(cmd.Cmd):
	intro = ""
	prompt = "Weka ngoma *****"
    
    @docopt_cmd
	def do_song_find(self, arg):
		""" Find a song using any given query
		Usage : song_find<query>
		"""
		query = arg["<query>"]
		song_find(query)

    @docopt_cmd
	def do_song_view(self, arg):
		"""Views a song using track track_id
		   Usage : song_view<track_id>
		"""	
		track_id = arg["<track_id>"]
		song_view(track_id)

	@docopt_cmd
	def do_song_clear(self, arg):
		"""Clear all the songs from the database
		   Usage:no argument provided
		"""
		print "Are you sure you want to clear the entire database"
		song_clear()

	@docopt_cmd
	def	do_song_save(self, arg):
		"""
		Save a song to the database
		Usage:song_save<track_id>

		"""
		track_id = arg["<track_id>"]
		song_save(track_id)

    @docopt_cmd
    def quit(self, arg):
    	"""
        Exits the app
        Usage: quit
    	"""
    	exit()
if __name__ == '__main__':
	LyricsFinder.cmdloop()
