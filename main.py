import streamlit as st
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
# Authors: Kat, Rachel, Peterson

# Authentication - without user
cid = "fe57f3a50d42459bbc8a810e4f09944d"
secret = "d54e4bca8f0d4f51a34ac9c564599133"

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


#3 Pages
#Home/Intro Page - main
#Choose songs Page - SetUpPage
#Results Page  - ResultsPage

name = st.text_input('name of artist')

results = sp.search(q ='artist:' + name, type='artist')
items = results['artists']['items']
if len(items) > 0:
    artist = items[0]
    print(artist['name'], artist['images'][0]['url'])
    st.text(artist['name'])
    st.text(artist['images'][0]['url'])


