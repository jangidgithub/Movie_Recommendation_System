import streamlit as st
import pickle
import pandas as pd
import requests

# create recommend function

def recommend(name):
    try:
        name_index = movies[movies['title'] == name].index[0]
        distance = similarity[name_index]
        movie_list = sorted(list(enumerate(distance)),
                            reverse=True, key=lambda x: x[1])[1:8]

        recommended_movies = []
        recommended_movie_poster_path = []
        for i in movie_list:
            movie_id = movies.iloc[i[0]].movie_id

            recommended_movies.append(movies.iloc[i[0]].title)
            
            # for fetch poster movie id 

            recommended_movie_poster_path.append(fetch_poster(movie_id))

        return recommended_movies, recommended_movie_poster_path
    except:
        print("Ooops....!, NOT Found")

# create function for fetching movies poster 

def fetch_poster(movie_id):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US")
    data = response.json()

    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

# display the title of the project


st.title("Movie Recomndation System")

# create the list of movies

movie_data = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movie_data)

# load similarity

similarity = pickle.load(open("Similarity.pkl", "rb"))

# create a input box which use for the enter the recommended movie name

select_movie_name = st.selectbox(
    "How would you like to be Contain",
    movies['title'].values
)

# create button for recommended

if st.button("Recommend"):
    names,posters = recommend(select_movie_name)

    col1,col2,col3,col4,col5,col6 = st.columns(6)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[2])
        st.image(posters[2])
    with col3:
        st.text(names[3])
        st.image(posters[3])
    with col4:
        st.text(names[4])
        st.image(posters[4])
    with col5:
        st.text(names[5])
        st.image(posters[5])
    with col6:
        st.text(names[6])
        st.image(posters[6])
