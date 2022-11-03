import streamlit as st
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import numpy as np

bond_map = st.checkbox("See where all the Bond movies were shot.")

if bond_map:
    st.write("These maps show which films were shot in which countries")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Dr. No")
        dr_no = pd.DataFrame(
            np.array([
                [52.3555, -1.1743],
                [18.1096, -77.2975]]),
            columns=['lat', 'lon'])
        st.map(dr_no)

        st.subheader("Goldfinger")
        gf = pd.DataFrame(
            np.array([
                [52.3555, -1.1743],
                [46.8182, 8.2275],
                [37.0902, -95.7129]]),
            columns=['lat', 'lon'])
        st.map(gf)

    with col2:
        st.subheader("From Russia with Love")
        frwl = pd.DataFrame(
            np.array([
                [52.3555, -1.1743],
                [56.4907, -4.2026],
                [41.8719, 12.5674],
                [46.8182, 8.2275],
                [38.9637, 35.2433]]),
            columns=['lat', 'lon'])
        st.map(frwl)