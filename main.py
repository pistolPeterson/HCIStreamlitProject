import streamlit as st
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

#user classes
import MainPage as mp

# Authors: Kat, Rachel, Peterson

# Authentication - without user
cid = "fe57f3a50d42459bbc8a810e4f09944d"
secret = "d54e4bca8f0d4f51a34ac9c564599133"

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


# Streamlit code
st.title("Peterson Test Spotify ")



#page selector, choosing a page will go to a corresponding python file
pageSelect = st.selectbox("choose something", options=["Pop", "Rock", "Neo-Soul"])
if pageSelect == "Pop":
    x = mp.MainPage()

name = st.text_input('name of artist')


results = sp.search(q ='artist:' + name, type='artist')
items = results['artists']['items']
if len(items) > 0:
    artist = items[0]
    print(artist['name'], artist['images'][0]['url'])
    st.text(artist['name'])
    st.text(artist['images'][0]['url'])


