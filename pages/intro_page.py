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
    layout="wide",
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

def cs_sidebar():

    st.sidebar.markdown('''[<img src='data:image/png;base64,{}' class='img-fluid' width=32 height=32>](https://streamlit.io/)'''.format(img_to_bytes("logomark_website.png")), unsafe_allow_html=True)
    st.sidebar.header('Streamlit cheat sheet')

    st.sidebar.markdown('''
<small>Summary of the [docs](https://docs.streamlit.io/en/stable/api.html), as of [Streamlit v1.0.0](https://www.streamlit.io/).</small>
    ''', unsafe_allow_html=True)

    st.sidebar.markdown('__How to install and import__')

    st.sidebar.code('$ pip install streamlit')

    st.sidebar.markdown('Import convention')
    st.sidebar.code('>>> import streamlit as st')

    st.sidebar.markdown('__Add widgets to sidebar__')
    st.sidebar.code('''
st.sidebar.<widget>
>>> a = st.sidebar.radio(\'R:\',[1,2])
    ''')

    st.sidebar.markdown('__Command line__')
    st.sidebar.code('''
$ streamlit --help
$ streamlit run your_script.py
$ streamlit hello
$ streamlit config show
$ streamlit cache clear
$ streamlit docs
$ streamlit --version
    ''')

    st.sidebar.markdown('__Pre-release features__')
    st.sidebar.markdown('[Beta and experimental features](https://docs.streamlit.io/en/stable/api.html#beta-and-experimental-features)')
    st.sidebar.code('''
pip uninstall streamlit
pip install streamlit-nightly --upgrade
    ''')

    st.sidebar.markdown('''<small>[st.cheat_sheet v1.0.0](https://github.com/daniellewisDL/streamlit-cheat-sheet)  | Oct 2021</small>''', unsafe_allow_html=True)

    return None

##########################
# Main body of cheat sheet
##########################

def cs_body():
    # Magic commands

    col1, col2 = st.columns(2)
    col1.subeader('Ryan Paik')
    col1.code('''# Magic commands implicitly `st.write()`
\'\'\' _This_ is some __Markdown__ \'\'\'
a=3
'dataframe:', data
    ''')

    col2.subheader('Display interactive widgets')
    col2.code('''
st.button('Hit me')
st.download_button('On the dl', data)
st.checkbox('Check me out')
st.radio('Radio', [1,2,3])
st.selectbox('Select', [1,2,3])
st.multiselect('Multiselect', [1,2,3])
st.slider('Slide me', min_value=0, max_value=10)
st.select_slider('Slide to select', options=[1,'2'])
st.text_input('Enter some text')
st.number_input('Enter a number')
st.text_area('Area for textual entry')
st.date_input('Date input')
st.time_input('Time entry')
st.file_uploader('File uploader')
st.color_picker('Pick a color')
    ''')
    col2.write('Use widgets\' returned values in variables:')
    col2.code('''
>>> for i in range(int(st.number_input('Num:'))): foo()
>>> if st.sidebar.selectbox('I:',['f']) == 'f': b()
>>> my_slider_val = st.slider('Quinn Mallory', 1, 88)
>>> st.write(slider_val)
    ''')

    # Control flow

    col2.subheader('Control flow')
    col2.code('''
st.stop()
    ''')

    # Lay out your app

    col2.subheader('Lay out your app')
    col2.code('''
st.form('my_form_identifier')
st.form_submit_button('Submit to me')
st.container()
st.columns(spec)
>>> col1, col2 = st.columns(2)
>>> col1.subheader('Columnisation')
st.expander('Expander')
>>> with st.expander('Expand'):
>>>     st.write('Juicy deets')
    ''')

    col2.write('Batch widgets together in a form:')
    col2.code('''
>>> with st.form(key='my_form'):
>>> 	text_input = st.text_input(label='Enter some text')
>>> 	submit_button = st.form_submit_button(label='Submit')
    ''')

    # Display code

    col2.subheader('Display code')
    col2.code('''
st.echo()
>>> with st.echo():
>>>     st.write('Code will be executed and printed')
    ''')

    # Display progress and status

    col2.subheader('Display progress and status')
    col2.code('''
st.progress(progress_variable_1_to_100)
st.spinner()
>>> with st.spinner(text='In progress'):
>>>     time.sleep(5)
>>>     st.success('Done')
st.balloons()
st.error('Error message')
st.warning('Warning message')
st.info('Info message')
st.success('Success message')
st.exception(e)
    ''')

    # Placeholders, help, and options

    col2.subheader('Placeholders, help, and options')
    col2.code('''
st.empty()
>>> my_placeholder = st.empty()
>>> my_placeholder.text('Replaced!')
st.help(pandas.DataFrame)
st.get_option(key)
st.set_option(key, value)
st.set_page_config(layout='wide')
    ''')

    # Mutate data

    col2.subheader('Mutate data')
    col2.code('''
DeltaGenerator.add_rows(data)
>>> my_table = st.table(df1)
>>> my_table.add_rows(df2)
>>> my_chart = st.line_chart(df1)
>>> my_chart.add_rows(df2)
    ''')

    # Optimize performance

    col2.subheader('Optimize performance')
    col2.code('''
@st.cache
>>> @st.cache
... def fetch_and_clean_data(url):
...     # Mutate data at url
...     return data
>>> # Executes d1 as first time
>>> d1 = fetch_and_clean_data(ref1)
>>> # Does not execute d1; returns cached value, d1==d2
>>> d2 = fetch_and_clean_data(ref1)
>>> # Different arg, so function d1 executes
>>> d3 = fetch_and_clean_data(ref2)

    ''')

    col2.subheader('Other key parts of the API')
    col2.markdown('''
<small>[State API](https://docs.streamlit.io/en/stable/session_state_api.html)</small><br>
<small>[Theme option reference](https://docs.streamlit.io/en/stable/theme_options.html)</small><br>
<small>[Components API reference](https://docs.streamlit.io/en/stable/develop_streamlit_components.html)</small><br>
<small>[API cheat sheet](https://share.streamlit.io/daniellewisdl/streamlit-cheat-sheet/app.py)</small><br>
''', unsafe_allow_html=True)


    col3.subheader('test')

    toc = Toc(col3)
    # col2.title("Table of contents")
    col3.write("http://localhost:8502/#display-progress-and-status",  unsafe_allow_html=True)
    toc.header("Header 1")
    toc.header("Header 2")
    toc.generate()
# toc.subheader("Subheader 1")
# toc.subheader("Subheader 2")
# toc.generate()
    # return None



# Run main()

# if __name__ == '__main__':
#     main()


# def main():
def app():    
    # cs_sidebar()
    cs_body()
    return None
