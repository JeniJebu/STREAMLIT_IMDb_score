import streamlit as st
import pickle

import streamlit as st
import sklearn
import numpy as np
import pandas as pd

# Get the versions of the libraries
sklearn_version = sklearn.__version__
numpy_version = np.__version__
pandas_version = pd.__version__

# Display the versions using Streamlit
st.write(f"scikit-learn version: {sklearn_version}")
st.write(f"NumPy version: {numpy_version}")
st.write(f"Pandas version: {pandas_version}")

st.set_page_config(page_title='IMBb-Movie Success')

# Load the trained model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("Movie Success Prediction")
st.write("Enter the details of the movie:")

col1,col2=st.columns(2)

# Input fields for user to enter the movie details

with col1:
    num_critic_for_reviews = st.number_input("Number of Critic Reviews", min_value=0,max_value=813,value=400)
    duration = st.number_input("Duration (minutes)", min_value=0,max_value=511, value=120)
    director_facebook_likes = st.number_input("Director Facebook Likes", min_value=0,max_value=23000, value=5000)
    actor_3_facebook_likes = st.number_input("Actor 3 Facebook Likes", min_value=0,max_value=23000, value=5000)
    actor_1_facebook_likes = st.number_input("Actor 1 Facebook Likes", min_value=0,max_value=640000, value=25000)
    gross = st.number_input("Gross Revenue", min_value=0,max_value=760505800, value=100000000)
    num_voted_users = st.number_input("Number of Voted Users", min_value=0,max_value=1689764, value=1000000)
with col2:
    cast_total_facebook_likes = st.number_input("Cast Total Facebook Likes", min_value=0, max_value=657000,value=10000)
    facenumber_in_poster = st.number_input("Face Number in Poster", min_value=0,max_value=43, value=5)
    num_user_for_reviews = st.number_input("Number of User Reviews", min_value=0,max_value=5100, value=50)
    budget = st.number_input("Budget", min_value=0,max_value=12215500000, value=10000000000)
    title_year = st.number_input("Title Year", min_value=1900, max_value=2016, value=2000)
    actor_2_facebook_likes = st.number_input("Actor 2 Facebook Likes", min_value=0,max_value=137000,value=50000)

submitted=st.button('Predict')

if submitted:

    prediction= model.predict([[num_critic_for_reviews, duration, director_facebook_likes,
    actor_3_facebook_likes, actor_1_facebook_likes, gross,
    num_voted_users, cast_total_facebook_likes, facenumber_in_poster,
    num_user_for_reviews, budget, title_year, actor_2_facebook_likes]])

    if prediction[0] == 'Poor' or prediction[0] == 'Average':
        st.success("The movie is predicted not to be a success!")
    else:
        st.success("The movie is predicted to be a success!")

