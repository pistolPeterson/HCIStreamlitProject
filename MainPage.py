# code for main page using streamlit
import streamlit as st
class MainPage:

    def __init__(self):
        st.title("Can your favorite song be a bond song?")
        st.header("An HCI Class Project determined to check if the song you input can be similar to a Bond song")

        st.subheader("Find your song!")
        name_of_song = st.text_input("Name of the song, we'll try to give the closest song to it")