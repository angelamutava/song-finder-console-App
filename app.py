"""DJ WEKA NGOMA
 This application finds lyrics to songs using musixmatch api.
Usage:
	songfind <query>
	song_view <track_id>
	song_clear
	song_clear_single_song<track_id>
	song_save<track_id>
	
"""
import cmd
from docopt import docopt, DocoptExit
from song_lyrics_finder import *
from pyfiglet import figlet_format
from termcolor import cprint

def docopt_cmd(func):
	"""
	Decorator definition for the app.
	"""
	def fn(self, arg):
		try:
			opt = docopt(fn.__doc__, arg)
		except DocoptExit as e:
			msg = "Invalid Command."

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
	intro = cprint(figlet_format("DJ WEKA NGOMA", font="big"), "cyan")
	prompt = "<--Weka ngoma -->"

	@docopt_cmd
	def do_songfind(self, arg):
		"""Usage: songfind <query> """
		query = arg["<query>"]
		song_find(query)
		

	@docopt_cmd
	def do_song_view(self, arg):
		"""Usage: song_view <track_id>"""	
		track_id = arg["<track_id>"]
		if track_id.isalpha():
			print "Track id should contain numbers only"
		song_view(track_id)

	@docopt_cmd
	def do_song_clear(self, arg):
		"""Usage: song_clear
		"""
		print "Are you sure you want to clear the entire database?"
		song_clear()

	@docopt_cmd
	def	do_song_save(self, arg):
		"""Usage: song_save <track_id>"""
		track_id = arg["<track_id>"]
		if track_id.isalpha():
			print "track id should contain numbers only"
		song_save(track_id)

	@docopt_cmd
	def do_song_clear_single_song(self, arg):
		"""Usage: song_clear_single_song <track_id>"""
		track_id = arg["<track_id>"]
		song_clear_single_song(track_id)

	
	def quit(self, arg):
		"""
	    Exits the app
	    Usage: quit
	    """
		exit()
if __name__ == '__main__':
	LyricsFinder().cmdloop()
