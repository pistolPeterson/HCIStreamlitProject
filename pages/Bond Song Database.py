import streamlit as st
import pandas as pd
import numpy as np
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import csv
cid = "fe57f3a50d42459bbc8a810e4f09944d"
secret = "d54e4bca8f0d4f51a34ac9c564599133"

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)



#read from track library and place it into a list called results
results = []
with open('csv/track_library.csv', newline='') as inputfile:
    for row in csv.reader(inputfile):
        results.append(row[0])


#if the spotifyuri doesnt show a preview link, remove it from the results list
for spotify_uri in results:
    if sp.track(spotify_uri)['preview_url'] is None:
        results.remove(spotify_uri)

name_of_uri = results
for i in range(0, len(name_of_uri)):
    name_of_uri[i] = sp.track(results[i])['name']

#place the results in streamlit multiselct widget
options = st.multiselect(
    'What samples do you want to listen to?',
    name_of_uri)

#show what the user selected
for x in options:
    #convert name back to a uri
    searched_track = sp.search(x, limit=1, offset=0, type='track', market=None)
    st.write(sp.track(searched_track['name'])['preview_url'])

