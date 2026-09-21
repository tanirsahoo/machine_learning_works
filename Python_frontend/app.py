import streamlit as st
import pickle
# from streamlit_option_menu import option_menu

movies_list = pickle.load(open('movies.pkl', 'rb'))
movies_list = movies_list['title'].values

st.title("Movie recommendation system")
options = st.selectbox(
    "Select a movie",
    movies_list
)