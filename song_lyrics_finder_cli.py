import click
from song_lyrics_finder import *

@click.group()
@click.command()
@click.option('--name', prompt='Your name please.')

def hello(name):
	click.secho('Hello %s Welcome to lyrics finder' % name, fg = "green")