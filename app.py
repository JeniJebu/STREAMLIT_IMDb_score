import streamlit as st
import pickle
import numpy as np

import streamlit as st
import sklearn

# Get the version of scikit-learn
sklearn_version = sklearn.__version__

# Display the version using Streamlit
st.write(f"The version of scikit-learn installed is: {sklearn_version}")


# Load the trained model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)



st.title("Movie Success Prediction")
st.write("Enter the details of the movie:")

# Input fields for user to enter the movie details
num_critic_for_reviews = st.number_input("Number of Critic Reviews", min_value=0,max_value=1000,value=0)
duration = st.number_input("Duration (minutes)", min_value=0,max_value=550, value=120)
director_facebook_likes = st.number_input("Director Facebook Likes", min_value=0,max_value=1e6, value=5000)
actor_3_facebook_likes = st.number_input("Actor 3 Facebook Likes", min_value=0,max_value=1e6, value=5000)
actor_1_facebook_likes = st.number_input("Actor 1 Facebook Likes", min_value=0,max_value=1e6, value=5000)
gross = st.number_input("Gross Revenue", min_value=0,max_value=1e10, value=5000)
num_voted_users = st.number_input("Number of Voted Users", min_value=0,max_value=1000, value=0)
cast_total_facebook_likes = st.number_input("Cast Total Facebook Likes", min_value=0, max_value=5000,value=0)
facenumber_in_poster = st.number_input("Face Number in Poster", min_value=0,max_value=200, value=0)
num_user_for_reviews = st.number_input("Number of User Reviews", min_value=0,max_value=1000, value=0)
budget = st.number_input("Budget", min_value=0,max_value=1e10, value=0)
title_year = st.number_input("Title Year", min_value=1900, max_value=2024, value=2000)
actor_2_facebook_likes = st.number_input("Actor 2 Facebook Likes", min_value=0,max_value=25000 ,value=0)

# Collect all inputs into a list
input_features = [
    num_critic_for_reviews, duration, director_facebook_likes,
    actor_3_facebook_likes, actor_1_facebook_likes, gross,
    num_voted_users, cast_total_facebook_likes, facenumber_in_poster,
    num_user_for_reviews, budget, title_year, actor_2_facebook_likes
]
submitted=st.button('Predict')

if submitted:
    pickled_model = pickle.load(open('model.pkl','rb'))
    prediction= pickled_model.predict(input_features)
    if prediction[0]=='Poor'|'Average':
        st.write("The movie is predicted not to be a success!")
        
    else:
        st.write("The movie is predicted to be a success!")

