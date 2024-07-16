import streamlit as st
import pickle
import pandas as pd
import requests

movies_list=pickle.load(open('movie_dict.pkl','rb'))
similarity=pickle.load(open('similarity.pkl', 'rb'))
movies=pd.DataFrame(movies_list)
st.title('Movie Recommender System')

# def fetch_poster(movie_id):
#     url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
#     data = requests.get(url)
#     data=data.json()
#     return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distance=similarity[movie_index]
    movie_list=sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies=[]
    # recommended_movies_posters=[]
    for i in movie_list:
        movie_id=movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        # #fetch poster with the help of API
        # recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies
option=st.selectbox(
    'Choose any movie!',
    movies['title'].values
)

if st.button('Show Recommendations'):
    recommended_movies =recommend(option)
    for i in recommended_movies:
        st.write(i)
    