import pickle
import streamlit as st
import requests

books = pickle.load(open("books.pkl","rb"))


st.title("Book Recommender System")
st.header("Here You will Get Similar Books")
def get_name(text):
    ISBNs = books[books['Title']==text]['Recommended_Books'].values[0]
    for ISBN in ISBNs:
        try:
            title_container = st.container()
            col1, col2 = st.columns((2,6))
            with title_container:
                with col1:
                    st.image(f"http://covers.openlibrary.org/b/ISBN/{ISBN}-M.jpg")
                with col2:
                    response = requests.get(f"https://openlibrary.org/isbn/{ISBN}.json").json()
                    st.header(response["title"])
                    st.subheader("Publisher: "+response["publishers"][0])
                    try:
                        genres = ', '.join(response["genres"])
                        st.subheader("Genres: "+genres)
                    except:
                        pass
        except:
            pass

book_list = books["Title"].values
selected_book = st.selectbox("Select Your Book", book_list)

if st.button('Search'):
    get_name(selected_book)
