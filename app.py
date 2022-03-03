import os
import streamlit as st
import numpy as np
from PIL import  Image
from modules.toc import *
# Custom imports 
from multipage import MultiPage
from pages import data_upload, cheatsheet_templ, streamlit_cheatsheet, machine_learning, metadata, data_visualize, redundant # import your pages here

# CONFIG
# st.set_page_config(
#     page_title='Streamlit cheat sheet',
#     layout="wide",
#     #  initial_sidebar_state="expanded",
# )

# Create an instance of the app 
app = MultiPage()

# Title of the main page
display = Image.open('Logo.png')
display = np.array(display)
# st.image(display, width = 400)
# st.title("Data Storyteller Application")
# col1, col2 = st.beta_columns(2)
col1, col2, col3= st.columns(3)
col1.image(display, width = 400)
col2.title("Data Storyteller Application")


# toc = Toc(col3)

# col3.title("Table of contents")
# col3.write("http://localhost:8502/#display-progress-and-status")
# toc.header("Header 1")
# toc.header("Header 2")
# toc.subheader("Subheader 1")
# toc.subheader("Subheader 2")
# toc.generate()


# Add all your application here
app.add_page("Ryan Paik", intro_page.app)
app.add_page('Streamlit CheatSheet', cheatsheet_templ.app)
app.add_page("Upload Data", data_upload.app)
app.add_page("Change Metadata", metadata.app)
# app.add_page("Machine Learning", machine_learning.app)
app.add_page("Data Analysis",data_visualize.app)
app.add_page("Y-Parameter Optimization",redundant.app)

# The main app
app.run()
