import streamlit as st
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import numpy as np

st.image('logo.png')
txt = st.text_area('', '''Jump into the world of James Bond, whose musical scores have shaped the cinematic and musical industries for decades. If you're a fan, you'll have a blast rediscovering some of your favorite tracks—and perhaps, even find some new ones. 
    ''')
st.caption('Presented to you by Rachel Quijano, Peterson Normil, and Kathryna Reiz')