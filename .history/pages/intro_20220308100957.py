"""
Off Multipage Cheatsheet
https://github.com/daniellewisDL/streamlit-cheat-sheet
@daniellewisDL : https://github.com/daniellewisDL

"""

import streamlit as st
from pathlib import Path
import base64
from modules.toc import *
# Initial page config

st.set_page_config(
    page_title='Code Compendium Intro Page',
    layout="wide"
    #  initial_sidebar_state="expanded",
)



# col2.title("Table of contents")
# col2.write("http://localhost:8502/#display-progress-and-status")
# toc.header("Header 1")
# toc.header("Header 2")
# toc.subheader("Subheader 1")
# toc.subheader("Subheader 2")
# toc.generate()



# Thanks to streamlitopedia for the following code snippet

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

# sidebar

# def cs_sidebar():

#     st.sidebar.markdown('''[<img src='data:image/png;base64,{}' class='img-fluid' width=32 height=32>](https://streamlit.io/)'''.format(img_to_bytes("logomark_website.png")), unsafe_allow_html=True)
#     st.sidebar.header('Streamlit cheat sheet')

#     st.sidebar.markdown('''
# <small>Summary of the [docs](https://docs.streamlit.io/en/stable/api.html), as of [Streamlit v1.0.0](https://www.streamlit.io/).</small>
#     ''', unsafe_allow_html=True)

#     st.sidebar.markdown('__How to install and import__')

#     st.sidebar.code('$ pip install streamlit')

#     st.sidebar.markdown('Import convention')
#     st.sidebar.code('>>> import streamlit as st')

#     st.sidebar.markdown('__Add widgets to sidebar__')
#     st.sidebar.code('''
# st.sidebar.<widget>
# >>> a = st.sidebar.radio(\'R:\',[1,2])
#     ''')

#     st.sidebar.markdown('__Command line__')
#     st.sidebar.code('''
# $ streamlit --help
# $ streamlit run your_script.py
# $ streamlit hello
# $ streamlit config show
# $ streamlit cache clear
# $ streamlit docs
# $ streamlit --version
#     ''')

#     st.sidebar.markdown('__Pre-release features__')
#     st.sidebar.markdown('[Beta and experimental features](https://docs.streamlit.io/en/stable/api.html#beta-and-experimental-features)')
#     st.sidebar.code('''
# pip uninstall streamlit
# pip install streamlit-nightly --upgrade
#     ''')

#     st.sidebar.markdown('''<small>[st.cheat_sheet v1.0.0](https://github.com/daniellewisDL/streamlit-cheat-sheet)  | Oct 2021</small>''', unsafe_allow_html=True)

#     return None

##########################
# Main body of cheat sheet
##########################

def cs_body():
    # col1 = st.columns(1)
    st.title("Ryan Paik's Coding Compendium")

    st.markdown('''
        ----------
        #### “*You don't learn to walk by following rules. You learn by doing, and by falling over.*”   
        ##### ~ Richard Branson
        --------
    ''')

    st.subheader("Welcome to my Code Compendium.")
    st.markdown('''
This website/webapp is my personal cheatsheet for of all the code snippets that I have needed over the past 2 years. This ended up being a quick detour into Streamlit while I was building flask api's.   

-----

#### **Programming is only as deep as you want to dive in.**
i
This webapp features the basic code snippets from all the "googling" from programming I have done. 

I have taken the plunge and have created my own markdown notebooks organizing information from quick solution tidbits to documentation for programming languages. 



Please visit my github for practical code and my research notebooks:

*[rypaik (Ryan Paik) · GitHub](https://github.com/rypaik)*

If you would like access to my Gist please email me.

ryanpaik@protonmail.com

-------

##### **Bio:**

Currently a Sophomore at University of Illinois at Urbana-Champaign.   
I am working Nights on my Bachelor's of Science in Systems Engineering and Design


##### **Hobbies:**

Trying to become a real guitar hero minus the game system, playing Valorant with the St Mark's crew, getting interesting eats no matter where I am, and playing toss with my baseball field rat of a cousin.  
The newest hobby is figuring out what I can build with all the new breakthroughs in technology.   
  

##### **Currently Working On:**

##### Frameworks and Languages:
    - Flask, Django, FastAPI, PyTorch, Streamlit, OpenCV,  shell scripting, Python, C++  

##### Databases:  
    - Postgres, Redis, MongoDB, and applicable ORMs

##### When I can  get up for Air:
    - React, swift(ios), Rust, GO!!  
    - Find a team to get a paper In ARXIV



**This site will be constantly updated as long as I program. Feel free to pass on the URL.**

    ''')

# def main():
def app():    
    # cs_sidebar()
    cs_body()
    return None
