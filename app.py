"""DJ WEKA NGOMA
 This application finds lyrics to songs using musixmatch api.
Usage:
	find <query>
	view <track_id>
	clear
	clear_song<track_id>
	save<track_id>
	
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
	intro = cprint(figlet_format("DJ   WEKA   NGOMA", font="big"), "yellow", attrs=['bold'])
	print "**********User Guide************"
	print "    Command    Description     Parameter"
	print "    find       finds  song     forever"
	print "    view       Gets lyrics     15445219"
	print "    clear      Clears db       No parameter"
	print "    clear_song Clears song     15445219"
	print "    save       Saves song      15445219"
	print "type --help-- to view commands"
	prompt = "<--Weka ngoma -->"

	@docopt_cmd
	def do_find(self, arg):
		"""Usage: find <query> """
		query = arg["<query>"]
		song_find(query)
		

	@docopt_cmd
	def do_view(self, arg):
		"""Usage: view <track_id>"""	
		track_id = arg["<track_id>"]
		if track_id.isalpha():
			print "Track id should contain numbers only"
		song_view(track_id)

	@docopt_cmd
	def do_clear(self, arg):
		"""Usage: clear
		"""
		song_clear()

	@docopt_cmd
	def	do_save(self, arg):
		"""Usage: save <track_id>"""
		track_id = arg["<track_id>"]
		if track_id.isalpha():
			print "track id should contain numbers only"
		song_save(track_id)

	@docopt_cmd
	def do_clear_song(self, arg):
		"""Usage: clear_song <track_id>"""
		track_id = arg["<track_id>"]
		song_clear_single_song(track_id)

	
	def do_quit(self, arg):
		"""Exits the application
	    """
		print "Welcome again!"
		exit()
if __name__ == '__main__':
	LyricsFinder().cmdloop()
