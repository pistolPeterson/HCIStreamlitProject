import streamlit as st
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import numpy as np

# Authors: Kat, Rachel, Peterson

# Authentication - without user
cid = "fe57f3a50d42459bbc8a810e4f09944d"
secret = "d54e4bca8f0d4f51a34ac9c564599133"

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)



#Used to get the features of the library songs, stored them in a file so this code is no longer needed
library_uris = np.loadtxt("csv/track_library.csv", dtype="str")


song_library_features = []

for uri in library_uris:
    track = sp.track(uri)
    song_library_features.append(sp.audio_features(uri)[0])

# User Interaction

st.title("Is this song a James Bond song?")
st.header("Look up a song from Spotify and we will analyze its 'James Bondness'")

#Ask the user for input
song_input = st.text_input('Enter the name of your song.')

#get the results based on the search query q
song_results =  sp.search(q ='track:' + song_input, type='track')

#get the items array of the result query
items_array = song_results["tracks"]["items"]

#specify the first result as our chosen song
song_uri = items_array[0]['uri']


#if the song uri has been acquired
if song_input:
    if song_uri:
        # get the track object from the given uri
        song = sp.track(song_uri)
        artist_info = song['artists']
        st.write('You have chosen the song:', song['name'], "by", artist_info[0]['name'])
        st.write('Here are some of your songs categories')
        song_features = sp.audio_features(song_uri)[0]
        st.write(song_features)


        st.write("We will now analyze your song's details with our library, please wait!")

        danceability = st.checkbox("View danceability")


        st.write(song_library_features[0]['danceability'])

    else:
        st.write("Sorry, we could not find that song on our database :( Please try a different search!")




#bondData = pd.read_csv('JamesBondInformationCSV.csv')
#st.dataframe(bondData)

