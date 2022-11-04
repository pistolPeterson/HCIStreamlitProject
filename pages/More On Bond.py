import streamlit as st
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import numpy as np

table = pd.read_csv('csv/bond info.csv')

st.title("The History of 007 Music")
st.header("'The Name's Bond. James Bond.'")

radio_names = ['Timeline', 'In Detail']
radio = st.radio('', radio_names)

number_of_movies = 0

if radio == 'Timeline':
    min_year = int(table['Year'].min())
    max_year = int(table['Year'].max())
    timeline = st.slider("Pick a year",
                         min_year, max_year)

    for index, song in table.iterrows():
        if table['Year'][index] == timeline:
            st.write(table['Title song'][index], "was written in", table['Year'][index], "for", table['Film'][index])
            number_of_movies += 1
    if number_of_movies is 0:
            st.write("No James Bond movie was released at this time.")
else:
    st.dataframe(table)
    st.caption('Films sorted by release date.')

st.header("Where were all the Bond movies shot?")

map_data = pd.DataFrame(
    np.array([
        [52.3555, -1.1743],
        [18.1096, -77.2975],
        [52.3555, -1.1743],
        [46.8182, 8.2275],
        [37.0902, -95.7129],
        [52.3555, -1.1743],
        [22.3193, 114.1694],
        [36.1408, -5.3536],
        [36.2048, 138.2529],
        [40.4637, -3.7492],
        [60.4720, 8.4689],
        [52.3555, -1.1743],
        [46.2276, 2.2137],
        [51.1657, 10.4515],
        [52.1326, 5.2913],
        [37.0902, -95.7129],
        [52.3555, -1.1743],
        [15.8700, 100.9925],
        [22.3193, 114.1694],
        [22.1910, 113.5360],
        [52.3555, -1.1743],
        [46.2276, 2.2137],
        [41.8719, 12.5674],
        [37.0902, -95.7129],
        [14.2350, -51.9253],
        [15.7835, -90.2308],
        [52.3555, -1.1743],
        [39.8078, -74.9312],
        [20.5937, 78.9629],
        [52.3555, -1.1743],
        [51.1657, 10.4515],
        [47.5162, 14.5501],
        [41.8719, 12.5674],
        [31.7917, -7.0926],
        [52.3555, -1.1743],
        [56.4907, -4.2026],
        [41.8719, 12.5674],
        [46.8182, 8.2275],
        [38.9637, 35.2433],
        [52.3555, -1.1743],
        [46.2276, 2.2137],
        [25.0343, -77.3963],
        [37.0902, -95.7129],
        [52.3555, -1.1743],
        [39.3999, -8.2245],
        [46.8182, 8.2275],
        [52.3555, -1.1743],
        [37.0902, -95.7129],
        [18.1096, -77.2975],
        [52.3555, -1.1743],
        [46.8182, 8.2275],
        [56.1304, -106.3468],
        [26.8206, 30.8025],
        [41.8719, 12.5674],
        [35.9375, 14.3754],
        [25.0343, -77.3963],
        [36.2048, 138.2529],
        [52.3555, -1.1743],
        [41.8719, 12.5674],
        [35.9375, 14.3754],
        [39.0742, 21.8243],
        [52.3555, -1.1743],
        [46.8182, 8.2275],
        [64.9631, -19.0208],
        [46.2276, 2.2137],
        [37.0902, -95.7129],
        [23.6345, -102.5528],
        [37.0902, -95.7129]]),
    columns=['lat', 'lon'])
st.map(map_data)
st.caption("This map shows which countries the films were shot in.")


