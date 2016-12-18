#Song lyrics finder
##(DJ WEKA NGOMA)

Song lyrics finder is a console application built using python. It levarages on the musixmatch API to get lyrics online.The user can find a song using a query of their choice. Being a fan of casting crown you can try out courageous.

####Installation.
Clone the repository.
```
https://github.com/anonymousme/bc-12-song-lyrics-finder 
```
In your virtual environment.
```
pip install -r requirements.txt
```
The above command will install the required libraries in order to get your environment up and running. Run app.py in the directory bc-12-song-lyrics-finder.

####Commands.
1.find<br/>
This command provided with a query finds all the top 10 hits with the given query. The API method that gets the song returns the top 10 hits with the given query.<br/>
######find courageous

2.save <br/>
This command saves a song to the database.Provided with the parameter song_id it gets the song lyrics online and saves them to the database.<br/>
######save 15445219

3.clear<br/>
This command clears the entire database.<br/>
######clear

4.clear_song<br/>
This command clears a song from the database using the song_id.<br/>
######clear_song 15445219

5.artist<br/>
This command gets the artist using artist name.It returns the artists with the given name based on the number passed in the url.
<br/>
######artist kari jobes

6.album<br/>
This command gets the album of songs based on the album_id passed to it.<br/>
######album 14250417

##User Interface 
On running python app.py the interface looks like this.<br/>
![alt](https://github.com/anonymousme/bc-12-song-lyrics-finder/blob/master/Capture.PNG "home")


##Suggestions on Improvements.
-Implement the song_lyrics_finder as a class.
-Implement tests for the methods.
CIAO!Angie Mutava---Aspiring Developer.