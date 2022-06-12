import streamlit as st
import json
import sys

sys.path.append('src/')
from callapi.apiTwitter import get_inital_data

def display_page():
    """
    Display page with streamlit
    Call get_initial_data when button was clicked to create a json file with tweets
    Display json file
    """
    word = st.text_input("word", value="", key="word", type="default", help="word to search in tweets", autocomplete=None, placeholder="France", disabled=False)
    page = st.number_input("page", min_value=1, max_value=None, value=1, key="page", help="how many page with 100 tweet you want", disabled=False)
    if st.button("search", key="search", help="search with twitter api"):
        get_inital_data(word, page)
        data = json.load(open("src/files/data.json"))
        st.json(data, expanded=True)

if __name__ == '__main__':
    display_page()
