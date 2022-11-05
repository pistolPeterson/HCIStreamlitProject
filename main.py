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


feature_variation_percentage = 0.50
library_matches_percentage = 0.50
overall_score_percentage = 0.80
number_of_features = 11
see_score = False


def isFeatureInBounds(libraryfeature, chosenSongFeature):
    upper_feature_range = libraryfeature + (
                libraryfeature * feature_variation_percentage)
    lower_feature_range = libraryfeature - (
                libraryfeature * feature_variation_percentage)
    return 1 if(chosenSongFeature >= abs(lower_feature_range) and chosenSongFeature <= abs(upper_feature_range)) else 0



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

    return matches

# User Interaction

st.title("Is this song a James Bond song?")
st.image('logo.png')
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
            st.write('Here are some of your songs statistics from Spotify!')
            song_features = sp.audio_features(song_uri)[0]
            st.write(song_features)

            library_popularities = np.loadtxt("csv/track_popularities", dtype="str")

            song_indexes = []
            for num in range(0, 24):
                song_indexes.append(num)

            chart_data = pd.DataFrame(
                library_popularities,
                columns=[1])

            st.bar_chart(chart_data)



            number_of_matches = 0

            number_of_matches += compareFeature('danceability', 0)


            number_of_matches += compareFeature('energy', 1)


            number_of_matches += compareFeature('key', 2)


            number_of_matches += compareFeature('loudness', 3)


            number_of_matches += compareFeature('mode', 4)

            number_of_matches += compareFeature('speechiness', 5)

            number_of_matches += compareFeature('acousticness', 6)

            number_of_matches += compareFeature('instrumentalness', 7)

            number_of_matches += compareFeature('liveness', 8)

            number_of_matches += compareFeature('valence', 9)

            number_of_matches += compareFeature('tempo', 10)

            overall_score = number_of_matches / (song_library_size * number_of_features)
            score_button = st.button("I'm ready to see my song's score!")
            if(score_button):
                st.write("Your song's 'James Bondness' is...")
                st.progress(overall_score)
                if overall_score >= overall_score_percentage:
                    st.balloons()
                st.write(int(overall_score * 100), "% !")


else:
    st.error("Sorry, we could not find that song on our database :( Please try a different search!")


#bondData = pd.read_csv('JamesBondInformationCSV.csv')
#st.dataframe(bondData)

