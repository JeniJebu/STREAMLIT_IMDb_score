import streamlit as st
import pickle

# Load the trained model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("Movie Success Prediction")

st.subheader('Review and Popularity')
col1,col2=st.columns(2)

# Input fields for user to enter the movie details
with col1:
    num_critic_for_reviews = st.number_input("Number of Critic Reviews", min_value=0,max_value=813,value=400)
    num_user_for_reviews = st.number_input("Number of User Reviews", min_value=0,max_value=5100, value=50)

with col2:
    num_voted_users = st.number_input("Number of Voted Users", min_value=0,max_value=1689764, value=1000000)

st.subheader('Social Media Likes')
col3,col4=st.columns(2)

with col3:
    director_facebook_likes = st.number_input("Director Facebook Likes", min_value=0,max_value=23000, value=5000)
    actor_1_facebook_likes = st.number_input("Actor 1 Facebook Likes", min_value=0,max_value=640000, value=25000)
    actor_3_facebook_likes = st.number_input("Actor 3 Facebook Likes", min_value=0,max_value=23000, value=5000)

with col4:
    actor_2_facebook_likes = st.number_input("Actor 2 Facebook Likes", min_value=0,max_value=137000,value=50000)
    movie_facebook_likes = st.number_input("Movie Facebook Likes", min_value=0, max_value=657000,value=10000)

st.subheader('Movie Details')
col5,col6=st.columns(2)

with col5:
    duration = st.number_input("Duration (minutes)", min_value=0,max_value=511, value=120)
    facenumber_in_poster = st.number_input("Number of Faces in Poster", min_value=0,max_value=43, value=5)
with col6:
    title_year = st.number_input("Title Year", min_value=1900, max_value=2016, value=2000)

st.subheader('Financials')
col7,col8=st.columns(2)

with col7:
    gross = st.number_input("Gross Earnings", min_value=0,max_value=760505800, value=100000000)
with col8:
    budget = st.number_input("Budget", min_value=0,max_value=12215500000, value=10000000000)


submitted=st.button('Predict')

if submitted:
    pickled_model = pickle.load(open('model.pkl','rb'))
    prediction= pickled_model.predict([[num_critic_for_reviews, duration, director_facebook_likes,
    actor_3_facebook_likes, actor_1_facebook_likes, gross,
    num_voted_users, movie_facebook_likes, facenumber_in_poster,
    num_user_for_reviews, budget, title_year, actor_2_facebook_likes]])

    if prediction[0] == 'Poor' or prediction[0] == 'Average':
        st.success("The movie is predicted not to be a success!")
    else:
        st.success("The movie is predicted to be a success!")