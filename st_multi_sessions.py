import os
import streamlit as st
import numpy as np
from PIL import Image
from modules.toc import *
# Custom imports 
from multipage import MultiPage

# import your pages here
from pages import intro, postgres


# st.set_page_config(layout="wide")
# Create an instance of the app 
app = MultiPage()

# Title of the main page
display = Image.open('rp_logo.png')
# display = np.array(display)
# st.image(display, width = 400)
# st.title("Data Storyteller Application")
# col1, col2 = st.beta_columns(2)
# col1, col2 = st.columns(2)

def increment_counter():
    st.session_state.count += 1

with st.container():
    col1 = st.columns(1)
    st.title('Counter Example using Callbacks')
    
    if 'count' not in st.session_state:
        st.session_state.count = 0
    
    st.button('Increment', on_click=increment_counter)
    st.write('Count = ', st.session_state.count)
   # st.image(display, width=400)
    # col1.image(display, width = 400)
    # col2.title("Ryan Paik Coding Compendium")


    # toc = Toc(col3)

    # col3.title("Table of contents")
    # col3.write("http://localhost:8502/#display-progress-and-status")
    # toc.header("Header 1")
    # toc.header("Header 2")
    # toc.subheader("Subheader 1")
    # toc.subheader("Subheader 2")
    # toc.generate()


    # Add all your application here
    app.add_page('Code Compendiumg Menu Page', intro.app )
    app.add_page('Postgres Cheatsheet for Python', postgres.app)



# The main app
app.run()
