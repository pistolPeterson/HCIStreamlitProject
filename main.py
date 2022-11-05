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
#library_uris = np.loadtxt("csv/track_library.csv", dtype="str")

#song_library_features = []

#for uri in library_uris:
#    track = sp.track(uri)
#    song_library_features.append(sp.audio_features(uri)[0])


song_library_features = pd.read_csv('csv/track_features.csv', sep=',', header=None)
song_library_size = len(song_library_features)


feature_variation_percentage = 0.35
library_matches_percentage = 0.50
number_of_matches = 0


def isFeatureInBounds(libraryfeature, chosenSongFeature):
    upper_feature_range = libraryfeature + (
                libraryfeature * feature_variation_percentage)
    lower_feature_range = libraryfeature - (
                libraryfeature * feature_variation_percentage)
    return 1 if(chosenSongFeature >= lower_feature_range and chosenSongFeature <= upper_feature_range) else 0



def compareFeature(featureName, featureIndex):
    matches = 0
    # get the chosen song's feature
    songFeature = song_features[featureName]

    # iterating through the specified feature of all library songs
    for index, song in song_library_features.iterrows():
        # getting the library feature
        currentLibrarySongFeature = song[featureIndex]
        print(currentLibrarySongFeature, songFeature)
        matches += isFeatureInBounds(currentLibrarySongFeature, songFeature)

    st.write("The song matches", matches, "of the songs in our library of",
             song_library_size, "songs")

    #if the number of matches to the library exceeds or equals the given percentage value
    if matches / song_library_size >= library_matches_percentage:
        st.success(("This song matches in", featureName, " to our library!"))
    else:
        st.warning(("This song does NOT match in", featureName, " to our library!"))


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
if len(items_array) > 0:
    song_uri = items_array[0]['uri']

    #if the song uri has been acquired and the input is correct
    if song_input:
        if song_uri:
            # get the track object from the given uri
            song = sp.track(song_uri)
            artist_info = song['artists']
            st.write('You have chosen the song:', song['name'], "by", artist_info[0]['name'])
            st.write('Here are some of your songs categories')
            song_features = sp.audio_features(song_uri)[0]
            st.write(song_features)

            danceability = st.checkbox("View Danceability")
            if(danceability):
                compareFeature('danceability', 0)

            energy = st.checkbox("View Energy")
            if(energy):
               compareFeature('energy', 1)

            key = st.checkbox("View Key")
            if(key):
                compareFeature('key', 2)

            loudness = st.checkbox("View Loudness")
            if(loudness):
               compareFeature('loudness', 3)

            mode = st.checkbox("View Mode")
            if(mode):
               compareFeature('mode', 4)

            speechiness = st.checkbox("View Speechiness")
            if(speechiness):
              compareFeature('speechiness', 5)

            acousticness = st.checkbox("View Acousticness")
            if(acousticness):
                compareFeature('acousticness', 6)

            instrumentalness = st.checkbox("View Instrumentalness")
            if(instrumentalness):
                compareFeature('instrumentalness', 7)

            liveness = st.checkbox("View Liveness")
            if(liveness):
                compareFeature('liveness', 8)

            valence = st.checkbox("View Valence")
            if(valence):
                compareFeature('valence', 9)

            tempo = st.checkbox("View Tempo")
            if(tempo):
                compareFeature('tempo', 10)
else:
    st.error("Sorry, we could not find that song on our database :( Please try a different search!")


#bondData = pd.read_csv('JamesBondInformationCSV.csv')
#st.dataframe(bondData)

