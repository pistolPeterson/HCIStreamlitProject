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




bondData = pd.read_csv('JamesBondInformationCSV.csv')
st.dataframe(bondData)

