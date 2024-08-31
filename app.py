import streamlit as st
import numpy as np
import pandas as pd
import pickle
import requests

def fetch_api(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=2278a2066c531f9f2fef0203137c3ea8".format(movie_id)
    data_request = requests.get(url)
    data = data_request.json()
    data = data['poster_path']

    full_path = "https://image.tmdb.org/t/p/w500/" + data
    return full_path



def recommender(option):

    index = movies[movies['title'] == option].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])[1:11]
    recommendation_list = []
    recommendation_poster =[]
    for i in distances:
     movie_id = movies.iloc[i[0]].id
     recommendation_list.append(movies.iloc[i[0]].title)
     recommendation_poster.append(fetch_api(movie_id))
    return recommendation_list, recommendation_poster


similarity = pickle.load(open('similarity.pkl','rb'))
movies_list = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_list)



st.title('Movie Recommender System')





option = st.selectbox(
    "How would you like to be contacted?",
    (movies['title'].values),
)

if st.button("Recommende"):
    recommendation_list , recommendation_poster =recommender(option)
    col1, col2, col3 , col4 , col5 = st.columns(5)

    with col1:
        st.text( recommendation_list[0])
        st.image(recommendation_poster[0])

    with col2:
        st.text( recommendation_list[1])
        st.image(recommendation_poster[1])

    with col3:
        st.text( recommendation_list[2])
        st.image(recommendation_poster[2])

    with col4:
        st.text( recommendation_list[3])
        st.image(recommendation_poster[3])

    with col5:
        st.text( recommendation_list[4])
        st.image(recommendation_poster[4])

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(recommendation_list[5])
        st.image(recommendation_poster[5])

    with col2:
        st.text(recommendation_list[6])
        st.image(recommendation_poster[6])

    with col3:
        st.text(recommendation_list[7])
        st.image(recommendation_poster[7])

    with col4:
        st.text(recommendation_list[8])
        st.image(recommendation_poster[8])

    with col5:
        st.text(recommendation_list[8])
        st.image(recommendation_poster[8])
