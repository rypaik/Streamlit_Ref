# Postgres Cheatsheet

MACOSX: if you used brew install

**Start, Stop, Restart, Login**

```Bash
# start postgres
brew services start postgres
pg_ctl -D /opt/homebrew/var/postgres start



# stop postgres
brew services stop postgres

# restart postgres
brew services restart postgres

# when starting for a new database
pqsl postgres
psql postgres -U myuser



# Login to Postgres database 
# enters into postgres command line
psql <database>

# version
postgres --v

# POSTGRES login and DB permissions
CREATE ROLE myuser WITH LOGIN;
ALTER ROLE myuser CREATEDB;


# in .env file for NodeJS
PG_CONNECTION_STRING=postgres://myuser@localhost/mydatabase
```

Commands work after logging into postgres

Prompt should be postgres=#

| **Command**                                      | **Description**                                                     | **Additional Information**                                                                                 |
| ------------------------------------------------ | ------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| psql -d database -U user -W                      | Connects to a database under a specific user                        | \-d: used to state the database name <br>-U:used to state the database user                                |
| psql -h host -d database -U user -W              | Connect to a database that resides on another host                  | \-h: used to state the host <br>-d: used to state the database name <br>-U:used to state the database user |
| psql -U user -h host “dbname=db sslmode=require” | Use SSL mode for the connection                                     | \-h: used to state the host <br>-U:used to state the database user                                         |
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

| **PostgreSQL Data Types** |                       |           |                    |             |
| ------------------------- | --------------------- | --------- | ------------------ | ----------- |
| Numeric                   | Character             | Date/Time | Monetary           | Binary      |
| Boolean                   | Geometric             | JSON      | Enumerated         | Text-Search |
| UUID                      | Network Address Types | Composite | Object Identifiers | Pseudo      |
| BitString                 | XML                   | Range     | Arrays             | pg_lsn      |

| **Operators**        |                         |
| -------------------- | ----------------------- |
| Arithmetic Operators | \+, -, *, /, %, ^, !    |
| Comparison Operators | =, !=, <>, >, <, >=, <= |
| Logical Operators    | AND, NOT, OR            |
| Bitwise Operators    | &,                      |

### Create a table

```Bash
mydb=# CREATE TABLE users (
  id BIGSERIAL PRIMARY KEY,
  firstName VARCHAR(200) NOT NULL,
  middleName VARCHAR(200) DEFAULT NULL,
  lastName VARCHAR(200) DEFAULT NULL
);


CREATE TABLE Student (
    roll INT,
    student_name VARCHAR,
    course VARCHAR,
    PRIMARY KEY(roll)
);
```

```python
# Get DB hostname


SELECT boot_val, reset_val
FROM pg_settings
WHERE name = 'listen_addresses';


# Get Ports
SELECT *
FROM pg_settings
WHERE name = 'port';


# https://stackoverflow.com/questions/5598517/find-the-host-name-and-port-using-psql-commands


# FROM BASH GET POSTGRES PORT
sudo netstat -plunt |grep postgres


# changing password for user
# log into postgres
cd /data
psql postgres postgres
\password <user>
```

---

### Managing Databases

```python
# CREATE in bash
CREATE DATABASE [IF NOT EXISTS] db_name;


# delete base
DROP DATABASE [IF EXISTS] db_name;
```

---

### Managing Tables

Create

```sql
CREATE [TEMP] TABLE [IF NOT EXISTS] table_name(
   pk SERIAL PRIMARY KEY,
   c1 type(size) NOT NULL,
   c2 type(size) NULL,
   ...
);
```

### CRUD Operations

Columns Actions

```sql
# Add new colum
ALTER TABLE table_name ADD COLUMN new_column_name TYPE;

# Drop a column
ALTER TABLE table_name DROP COLUMN column_name;

# Rename a column
ALTER TABLE table_name RENAME column_name TO new_column_name;

# Set or remove default value of columnn
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

---

Create A View

```python
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

**Managing Indexes**

```python
# Creating an index with specified name on a table
CREATE [UNIQUE] INDEX index_name
ON table (column,...)


# Removing a specified index from a table
DROP INDEX index_name;
```

**Querying Data**

```python
# Query All Data
SELECT * FROM table_name;

# Query Data  from specific columns from all rows
SELECT column_list
FROM table;

# Query Data and sleect only unique rows
SELECT DISTINCT (column)
FROM table;

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

---

T
**Set Operations**

```python
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

---

**Modifying Data**

```python
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

---

**Performance**

```python
# Show the query plan for a query:
EXPLAIN query;


# Show and execute the query plan for a query:
EXPLAIN ANALYZE query;


# Collect statistics:
ANALYZE table_name;
```
