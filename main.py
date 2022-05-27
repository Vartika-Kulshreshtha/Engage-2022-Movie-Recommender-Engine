import streamlit as st
import pickle
import pandas as pd
import requests
from streamlit_lottie import st_lottie

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Watch Next", page_icon=":movie_camera:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# ---- LOAD ASSETS ----
lottie_hello = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_jmuq5aha.json")
lottie_coding = load_lottieurl("https://assets1.lottiefiles.com/private_files/lf30_bb9bkg1h.json")
lottie_contact = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_dhcsd5b5.json")

# ---- HEADER SECTION ----
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Hello this is Watch Next website :sunglasses:")
        st.title("A Movie Recommendation Engine")
        st.write(
            "Hello movie lovers I will help you to recommend movie according to your taste..."
        )

    with right_column:
        st_lottie(lottie_hello, height=250, key="hello")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            Are you feeling bored or tired and want to watch some movies according to your need or demand 
            so... don't worry I will help you with that.

            You only need to search a movie based on your mood and I will suggest you some more movies that you also
            might like it.

            A movie genre can be:
            - Drama :performing_arts:
            - Comedy :joy:
            - Action :clapper:
            - Fantasy :angel:
            - Horror :fearful:
            - Romance :love_letter:
            - Western :person_with_blond_hair:
            - Thriller :grimacing:

            """
        )
    with right_column:
        st_lottie(lottie_coding, height=400, key="coding")


def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=bc94c2896fe54026d162b9deab569083'
                            '&language=en-US'.format(movie_id))
    data = response.json()
    print(data)
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommend_movies = []
    recommend_movies_poster = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id

        recommend_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommend_movies_poster.append(fetch_poster(movie_id))
    return recommend_movies, recommend_movies_poster


st.header('Movie Recommender System')
movies_dict = pickle.load(open(r'C:\Users\Dell\OneDrive\Desktop\movie-recommender-system\venv\movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open(r'C:\Users\Dell\OneDrive\Desktop\movie-recommender-system\venv\similarity.pkl', 'rb'))

selected_movie_name = st.selectbox(
    "Type or select a movie from the dropdown", movies['title'].values
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.beta_columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/kulshreshthavartika00@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    <form action="https://formsubmit.co/kulshreshthavartika00@gmail.com" method="POST" />

    </form>


    """

    st.write("[Connect through LinkedIn >](https://www.linkedin.com/in/vartika-kulshreshtha-659157218/)")
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

with right_column:
    st_lottie(lottie_contact, height=300, key="contact")
