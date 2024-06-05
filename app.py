import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define the prediction function
def predict_success(features):
    input_features = np.array([features])
    prediction = model.predict(input_features)
    return prediction[0]

# Streamlit app
st.title("Movie Success Prediction")

st.write("Enter the details of the movie:")

# Input fields for user to enter the movie details
num_critic_for_reviews = st.number_input("Number of Critic Reviews", min_value=0, value=0)
duration = st.number_input("Duration (minutes)", min_value=0, value=0)
director_facebook_likes = st.number_input("Director Facebook Likes", min_value=0, value=0)
actor_3_facebook_likes = st.number_input("Actor 3 Facebook Likes", min_value=0, value=0)
actor_1_facebook_likes = st.number_input("Actor 1 Facebook Likes", min_value=0, value=0)
gross = st.number_input("Gross Revenue", min_value=0, value=0)
num_voted_users = st.number_input("Number of Voted Users", min_value=0, value=0)
cast_total_facebook_likes = st.number_input("Cast Total Facebook Likes", min_value=0, value=0)
facenumber_in_poster = st.number_input("Face Number in Poster", min_value=0, value=0)
num_user_for_reviews = st.number_input("Number of User Reviews", min_value=0, value=0)
budget = st.number_input("Budget", min_value=0, value=0)
title_year = st.number_input("Title Year", min_value=1900, max_value=2024, value=2000)
actor_2_facebook_likes = st.number_input("Actor 2 Facebook Likes", min_value=0, value=0)

# Collect all inputs into a list
input_features = [
    num_critic_for_reviews, duration, director_facebook_likes,
    actor_3_facebook_likes, actor_1_facebook_likes, gross,
    num_voted_users, cast_total_facebook_likes, facenumber_in_poster,
    num_user_for_reviews, budget, title_year, actor_2_facebook_likes
]

# Button to make the prediction
if st.button("Predict"):
    result = predict_success(input_features)
    st.write("The predicted IMDb binned score is:", result)
    if result in ['good', 'excellent']:
        st.write("The movie is predicted to be a success!")
    else:
        st.write("The movie is predicted not to be a success.")
