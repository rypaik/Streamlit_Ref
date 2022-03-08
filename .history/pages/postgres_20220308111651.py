import streamlit as st
from pathlib import Path
import base64
from modules.toc import *
# Initial page config

page_title ='Postgres Cheatsheet for Python'
# st.set_page_config(
#     page_title='Postgres Cheatsheet for Python',
#     layout="wide",
#     #  initial_sidebar_state="expanded",
# )

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded


##########################
# Main body of cheat sheet
##########################

def cs_body():
    
    page_title='Postgres for Python Cheatsheet',
    col1, col2= st.columns(2)
    
    col1.subheader('Getting Started')
    col1.markdown('''MACOSX: if you used brew install

**Start, Stop, Restart, Login**

```Bash
# START, STOP, RESTART postgres
brew services start postgres
pg_ctl -D /opt/homebrew/var/postgres start
brew services stop postgres
brew services restart postgres

# when starting for a new database
pqsl postgres
psql postgres -U myuser

# Login to Postgres database 
# enters into postgres command line
psql <database>

# POSTGRES login and DB permissions
CREATE ROLE myuser WITH LOGIN;
ALTER ROLE myuser CREATEDB;

# in .env file for NodeJS
PG_CONNECTION_STRING=postgres://myuser@localhost/mydatabase
```
Commands work after logging into postgres
Prompt should be postgres=#
''')

    # Display text

    col1.subheader('Display text')
    col1.code('''
st.text('Fixed width text')
st.markdown('_Markdown_') # see *
st.caption('Balloons. Hundreds of them...')
st.latex(r\'\'\' e^{i\pi} + 1 = 0 \'\'\')
st.write('Most objects') # df, err, func, keras!
st.write(['st', 'is <', 3]) # see *
st.title('My title')
st.header('My header')
st.subheader('My sub')
st.code('for i in range(8): foo()')

* optional kwarg unsafe_allow_html = True

    ''')

    # Display data

    col1.subheader('Display data')
    col1.code('''
st.dataframe(my_dataframe)
st.table(data.iloc[0:10])
st.json({'foo':'bar','fu':'ba'})
st.metric(label="Temp", value="273 K", delta="1.2 K")
    ''')

    # Display charts

    col1.subheader('Display charts')
    col1.code('''
st.line_chart(data)
st.area_chart(data)
st.bar_chart(data)
st.pyplot(fig)
st.altair_chart(data)
st.vega_lite_chart(data)
st.plotly_chart(data)
st.bokeh_chart(data)
st.pydeck_chart(data)
st.deck_gl_chart(data)
st.graphviz_chart(data)
st.map(data)
    ''')

    # Display media

    col1.subheader('Display media')
    col1.code('''
st.image('./header.png')
st.audio(data)
st.video(data)
    ''')

    # Display interactive widgets

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

    st.subheader("PSQL CLI Commands")
    st.markdown('''
                  
    Commands work after logging into postgres

Prompt should be postgres=#

| **Command**                                      | **Description**                                                     | **Additional Information**                                                                                 |
| ------------------------------------------------ | ------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| psql -d database -U user -W                      | Connects to a database under a specific user                        | \-d: used to state the database name <br>-U:used to state the database user                                |
| psql -h host -d database -U user -W              | Connect to a database that resides on another host                  | \-h: used to state the host <br>-d: used to state the database name <br>-U:used to state the database user |
| psql -U user -h host "dbname=db sslmode=require" | Use SSL mode for the connection                                     | \-h: used to state the host <br>-U:used to state the database user                                         |
| \c <dbname>                                      | Switch connection to a new database                                 |                                                                                                            |
| CREATE DATABASE <name>                           | Create a database                                                   |                                                                                                            |
| \l                                               | List available databases                                            |                                                                                                            |
| \d or \d+                                        | List all tables in database                                         |                                                                                                            |
| \dt or \dt+                                      | List available tables                                               |                                                                                                            |
| \d table_name                                    | Describe a table such as a column, type, modifiers of columns, etc. |                                                                                                            |
| \dn                                              | List all schemes of the currently connected database                |                                                                                                            |
| \df                                              | List available functions in the current database                    |                                                                                                            |
| \dv                                              | List available views in the current database                        |                                                                                                            |
| \du                                              | List all users and their assign roles                               |                                                                                                            |
| SELECT version();                                | Retrieve the current version of PostgreSQL server                   |                                                                                                            |
| \g                                               | Execute the last command again                                      |                                                                                                            |
| \s                                               | Display command history                                             |                                                                                                            |
| \s filename                                      | Save the command history to a file                                  |                                                                                                            |
| \i filename                                      | Execute psql commands from a file                                   |                                                                                                            |
| ?                                                | Know all available psql commands                                    |                                                                                                            |
| \h                                               | Get help                                                            | Eg:to get detailed information on ALTER TABLE statement use the \h ALTER TABLE                             |
| \e                                               | Edit command in your own editor                                     |                                                                                                            |
| \a                                               | Switch from aligned to non-aligned column output                    |                                                                                                            |
| \H                                               | Switch the output to HTML format                                    |                                                                                                            |
| \q                                               | Exit psql shell                                                     |                                                                                                            |
| select pg_gethostname();                         | PG Hostname                                                         | *BROKEN*                                                                                                   |
| \x                                               | show query out put in pretty format                                 |                                                                                                            |
    
    ''')

# def main():
def app():    
    # cs_sidebar()
    cs_body()
    return None
