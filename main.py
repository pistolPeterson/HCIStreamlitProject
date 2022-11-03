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


feature_variation_percentage = 0.25
library_matches_percentage = 0.50


def compareFeature(libraryfeature, chosenSongFeature):
    upper_feature_range = libraryfeature + (
                libraryfeature * feature_variation_percentage)
    lower_feature_range = libraryfeature - (
                libraryfeature * feature_variation_percentage)
    return 1 if(chosenSongFeature >= lower_feature_range and chosenSongFeature <= upper_feature_range) else 0


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

            danceability = st.checkbox("View danceability")

            #If the user has chosen to view the danceability feature
            if(danceability):
                number_of_danceability_matches = 0
                #get the chosen song's danceability
                song_danceability = song_features['danceability']
                #how many times does the chosen song match the library songs

                #iterating through all the danceabilities, column #0
                for index, song in song_library_features.iterrows():
                    #getting the danceability feature
                    currentLibrarySongFeature = song[0]
                    number_of_danceability_matches += compareFeature(song_danceability, currentLibrarySongFeature)
                st.write("The song matches", number_of_danceability_matches, "of the songs in our library of", song_library_size, "songs")
                if number_of_danceability_matches / song_library_size >= library_matches_percentage:
                    st.success("This song matches in danceability to our library!")
                else:
                    st.warning("This song does NOT match in danceability to our library!")

            energy = st.checkbox("View energy")
            if(energy):
                number_of_energy_matches = 0
                #get the chosen song's danceability
                song_energy = song_features['energy']
                #how many times does the chosen song match the library songs

                #iterating through all the danceabilities, column #0
                for index, song in song_library_features.iterrows():
                    #getting the danceability feature
                    currentLibrarySongFeature = song[0]
                    number_of_energy_matches += compareFeature(song_energy, currentLibrarySongFeature)
                st.write("The song matches", number_of_energy_matches, "of the songs in our library of", song_library_size, "songs")
                if number_of_energy_matches / song_library_size >= library_matches_percentage:
                    st.success("This song matches in energy to our library!")
                else:
                    st.warning("This song does NOT match in energy to our library!")


else:
    st.error("Sorry, we could not find that song on our database :( Please try a different search!")




#bondData = pd.read_csv('JamesBondInformationCSV.csv')
#st.dataframe(bondData)

