import streamlit as st
from pathlib import Path
import base64
from modules.toc import *
# Initial page config

page_title ='Postgres Cheatsheet for Python'
layout="wide"
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
    col1.write("")
    col1.subheader("**Start, Stop, Restart, Login**")
    col1.markdown('''
		```Bash
		# **MACOSX: Use Homebrew to Install**
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
``` sql

	CREATE [TEMP] TABLE [IF NOT EXISTS] table_name(
	pk SERIAL PRIMARY KEY,
	c1 type(size) NOT NULL,
	c2 type(size) NULL,

mydb=# CREATE TABLE users (
  id BIGSERIAL PRIMARY KEY,
  firstName VARCHAR(200) NOT NULL,
  middleName VARCHAR(200) DEFAULT NULL,
  lastName VARCHAR(200) DEFAULT NULL
);

# Another Convention
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
# Create a Table    
    col1.subheader('Managing Tables')
    col1.markdown('''
	``` sql
    # CREATE TABLE
	CREATE [TEMP] TABLE [IF NOT EXISTS] table_name(
		pk SERIAL PRIMARY KEY,
		c1 type(size) NOT NULL,
		c2 type(size) NULL,
  		);
    ```	
	''')
    
# Column Actions    
    col1.subheader("Column Actions")
    col1.markdown('''
	``` sql
	# Column Actions
	# Add new colum
	ALTER TABLE table_name ADD COLUMN new_column_name TYPE;

	# Drop a columnf
	ALTER TABLE table_name DROP COLUMN column_name;

	# Rename a column
	ALTER TABLE table_name RENAME column_name TO new_column_name;

	# Set or remove default value of column
	ALTER TABLE table_name ALTER COLUMN [SET DEFAULT value | DROP DEFAULT]

	# Add a primary key
	ALTER TABLE table_name ADD PRIMARY KEY (column,...);

	# Remove primary key
	ALTER TABLE table_name 
	DROP CONSTRAINT primary_key_constraint_name;

	# Rename a table
	ALTER TABLE table_name RENAME TO new_table_name;

	# Drop a table and dependent objects
	DROP TABLE [IF EXISTS] table_name CASCADE;
	```
	''')
    
    # Views    
    col1.subheader("Views")
    col1.markdown('''
	``` sql
	# Create a view
	CREATE OR REPLACE view_name AS
	query;

	# Create a Recursive View
	CREATE RECURSIVE VIEW view_name(column_list) AS
	SELECT column_list;

	# Create a Materialized View
	CREATE MATERIALIZED VIEW view_name
	AS
	query
	WITH [NO] DATA;

	# Refresh a Materialized view
	REFRESH MATERIALIZED VIEW CONCURRENTLY view_name;

	# Drop a view
	DROP VIEW [ IF EXISTS ] view_name;

	# Drop a Materalized view
	DROP MATERIALIZED VIEW view_name;

	# Rename a View
	ALTER VIEW view_name RENAME TO new_name;
	```
	''')
    
# Managing Indexes 
    col1.subheader("Managing Indexes")
    col1.markdown('''
	``` sql
	# Creating an index with specified name on a table
	CREATE [UNIQUE] INDEX index_name
	ON table (column,...)

	# Removing a specified index from a table
	DROP INDEX index_name;
	```
	''')
# Querying Data    
    col2.subheader("Querying Data")
    col2.markdown('''
``` sql
# Query All Data
SELECT * FROM table_name;
	
# Query Data  from specific columns from all rows
SELECT column_list
FROM table
	
# Query Data and sleect only unique rows
SELECT DISTINCT (column)
FROM table

# Query data from a table with a filter:
SELECT *
FROM table
WHERE condition;
SELECT * 
FROM table 
WHERE course='CS101';

# QUERY data from table with Limit Claus
SELECT * 
FROM table
LIMIT n;

# Assign an Alias to a column in Result Set
SELECT column_1 AS new_column_1, ...
FROM table;

# Query Data using LIKE operator
SELECT * FROM table_name
WHERE column LIKE '%value%'

# Query data using the BETWEEN operator
SELECT * FROM table_name
WHERE column BETWEEN low AND high;

# Query data using the IN operator:
SELECT * FROM table_name
WHERE column IN (value1, value2,...);

# Constrain the returned rows with the LIMIT clause:
SELECT * FROM table_name
LIMIT limit OFFSET offset
ORDER BY column_name;

# Query data from multiple using the inner join, left join, full outer join, cross join and natural join:
SELECT * 
FROM table1
INNER JOIN table2 ON conditions

SELECT * 
FROM table1
LEFT JOIN table2 ON conditions

SELECT * 
FROM table1
FULL OUTER JOIN table2 ON conditions

SELECT * 
FROM table1
CROSS JOIN table2;

SELECT * 
FROM table1
NATURAL JOIN table2;

# Return the number of rows of a table.
SELECT COUNT (*)
FROM table_name;

# Sort rows in ascending or descending order:
SELECT select_list
FROM table
ORDER BY column ASC [DESC], column2 ASC [DESC],...;

# Group rows using GROUP BY clause.
SELECT *
FROM table
GROUP BY column_1, column_2, ...;

# Filter groups using the HAVING clause.
SELECT *
FROM table
GROUP BY column_1
HAVING condition;
```
	''')

# Set Operations
    col2.subheader("Set Operations")
    col2.markdown('''
                  ``` sql
# Combine the result set of two or more queries with UNION operator:
SELECT * FROM table1
UNION
SELECT * FROM table2;


# Minus a result set using EXCEPT operator:
SELECT * FROM table1
EXCEPT
SELECT * FROM table2;


# Get intersection of the result sets of two queries:
SELECT * FROM table1
INTERSECT
SELECT * FROM table2;
```     
''')
    
    # Modifying Data
    col2.subheader("Modifying Data")
    col2.markdown('''
                  ``` sql
# Insert a new row into a table:
INSERT INTO table(column1,column2,...)
VALUES(value_1,value_2,...);

# Insert multiple rows into a table:
INSERT INTO 
    table_name(column1,column2,...)
VALUES
    (value_1,value_2,...),
    (value_1,value_2,...),
    (value_1,value_2,...);

# Update data for all rows:
UPDATE table_name
SET column_1 = value_1,
    ...;

# Update data for a set of rows specified by a condition in the WHERE clause.
UPDATE table
SET column_1 = value_1,
    ...
WHERE condition;

# can have multiple conditions
WHERE condition_1 AND condition_2;

# Delete all rows of a table:
DELETE FROM table_name;

# Delete specific rows based on a condition:
DELETE FROM table_name
WHERE condition;
```                  
''')
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
