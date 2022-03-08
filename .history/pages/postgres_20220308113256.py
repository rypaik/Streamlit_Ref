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


    # Display data

    col1.subheader('Creating a Table')
    col1.markdown('''
``` Bash
mydb=# CREATE TABLE users (
  id BIGSERIAL PRIMARY KEY,
  firstName VARCHAR(200) NOT NULL,
  middleName VARCHAR(200) DEFAULT NULL,
  lastName VARCHAR(200) DEFAULT NULL
);

# Another Convetnsion
CREATE TABLE Student (
	roll INT,
	student_name VARCHAR,
	course VARCHAR,
	PRIMARY KEY(roll)
);
```

``` python
# Get DB hostname

SELECT boot_val, reset_val
FROM pg_settings
WHERE name = 'listen_addresses';

# Get Ports
SELECT *
FROM pg_settings
WHERE name = 'port';

# FROM BASH GET POSTGRES PORT
sudo netstat -plunt | grep postgres

# changing password for user
# log into postgres then
cd /data
psql postgres postgres
\password <user>
```



    ''')

# Managing Databasee
    col1.subheader('Managing Databases')
    col1.markdown('''

    ```python
    # CREATE in bash
    CREATE DATABASE [IF NOT EXISTS] db_name;


    # delete base
    DROP DATABASE [IF EXISTS] db_name;
    ```
    
    ''')
    
     # COLUMN 2
 
 
 
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
| \ a                                               | Switch from aligned to non-aligned column output                    |                                                                                                            |
| \H                                               | Switch the output to HTML format                                    |                                                                                                            |
| \q                                               | Exit psql shell                                                     |                                                                                                            |
| select pg_gethostname();                         | PG Hostname                                                         | *BROKEN*                                                                                                   |
| \ x                                               | show query out put in pretty format                                 | NOTE: Escape sequence for streamlit                                                                       |
    
    ''')

# def main():
def app():    
    # cs_sidebar()
    cs_body()
    return None