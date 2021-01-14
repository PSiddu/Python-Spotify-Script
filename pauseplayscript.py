# While this script is running, your Spotify music can be paused/played from anywhere outside of the app
# by binding control to a specific key. This prevents the user from changing windows if they have to 
# turn on/off music frequently. (i.e. while studying)

# importing modules
import spotipy
import requests
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import os
# script must be run with sudo from terminal if using on Linux based OS
import keyboard

# Client ID, Secret, and Redirect URI as environment variables (for security purposes)
os.environ['SPOTIPY_CLIENT_ID'] = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
os.environ['SPOTIPY_CLIENT_SECRET'] = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
os.environ['SPOTIPY_REDIRECT_URI'] = 'https://www.spotify.com/ca-en/'

# makes use of token for authentication (login screen appears in browser when ran for first time)
scope = "user-read-playback-state,user-modify-playback-state"
spotify = spotipy.Spotify(client_credentials_manager=SpotifyOAuth(scope=scope))

status = spotify.currently_playing()

# If you haven't used Spotify for around a minute before running the script, then Spotify will not detect the
# device as online and the script can't work. Thus, this message will print instead, and the loop will break.
while True:
    if status == None:
        print("Start playing something on Spotify and rerun! :)")
        break
    # The while loop runs until the script is terminated. Toggle pause/play with whatever key-bind you 
    # wish to set. Currently, it is set to the "`" key, but this can be changed.
    if keyboard.is_pressed('`'):
        status = spotify.currently_playing()
        if status['is_playing'] == False:
            spotify.start_playback()
        elif status['is_playing'] == True:
            spotify.pause_playback()
