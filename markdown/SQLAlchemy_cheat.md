
# /Users/jb_mini/Projects/python/database/sqlalchemy_00.py
# database/sqlalchemy_00.py


### Setup

``` python
# import
import SQLAlchemy as db


# ** Setup and Connecting ** #
# engine = db.create_engine('dialect+driver://user:pass@host:port/db')
engine = db.create_engine('sqlite:///census.sqlite')
connection = engine.connect()
metadata = db.MetaData()
census = db.Table('census', metadata, autoload=True, autoload_with=engine)
```

### CRUD


### Reading and Viewing
``` python
# **** Viewing Table Details **** # 
# Print the column names
print(census.columns.keys())

# Print full table metadata
print(repr(metadata.tables['census']))

# **** FILTERING DATA **** #
# WHERE
# SQL :
SELECT * FROM census WHERE sex = F
#SQLAlchemy :
db.select([census]).where(census.columns.sex == 'F')

# SQL :
SELECT state, sex 
FROM census
WHERE state IN (Texas, New York)
# SQLAlchemy :
db.select([census.columns.state, census.columns.sex]).where(census.columns.state.in_(['Texas', 'New York']))

# AND OR NOT
# SQL :
SELECT * FROM census
WHERE state = 'California' AND NOT sex = 'M'
# SQLAlchemy :
db.select([census]).where(db.and_(census.columns.state == 'California', census.columns.sex != 'M'))

# ORDER BY
# SQL :
SELECT * FROM census
WHERE state = 'California' AND NOT sex = 'M'
# SQLAlchemy :
db.select([census]).where(db.and_(census.columns.state == 'California', census.columns.sex != 'M'))

# FUNCTIONS
# SQL :
SELECT SUM(pop2008)
FROM census
# SQLAlchemy :
db.select([db.func.sum(census.columns.pop2008)])

# GROUP BY
# SQL :
SELECT SUM(pop2008) as pop2008, sex
FROM census
# SQLAlchemy :
db.select([db.func.sum(census.columns.pop2008).label('pop2008'), census.columns.sex]).group_by(census.columns.sex)

# DISTINCT
# SQL :
SELECT DISTINCT state
FROM census
# SQLAlchemy :
db.select([census.columns.state.distinct()])

# CASE AND CAST
# The case() expression accepts a list of conditions to match and the column to return if the condition matches, followed by an else_ if none of the conditions match.
import sqlalchemy as db

engine = db.create_engine('sqlite:///census.sqlite')
connection = engine.connect()
metadata = db.MetaData()
census = db.Table('census', metadata, autoload=True, autoload_with=engine)

female_pop = db.func.sum(db.case([(census.columns.sex == 'F', census.columns.pop2000)],else_=0))

total_pop = db.cast(db.func.sum(census.columns.pop2000), db.Float)

query = db.select([female_pop/total_pop * 100])

result = connection.execute(query).scalar()
print(result)


# JOINS
# with 2 tables census and state_fact
select([census.columns.pop2008, state_fact.columns.abbreviation])

```

### Creating and Inserting
``` python
# **** CREATING INSERTING DATA INTO TABLES **** #
import sqlalchemy as db
import pandas as pd

# Creating Database and Table
engine = db.create_engine('sqlite:///test.sqlite') #Create test.sqlite automatically
connection = engine.connect()
metadata = db.MetaData()

emp = db.Table('emp', metadata,
              db.Column('Id', db.Integer()),
              db.Column('name', db.String(255), nullable=False),
              db.Column('salary', db.Float(), default=100.0),
              db.Column('active', db.Boolean(), default=True)
              )

metadata.create_all(engine) #Creates the table

# Inserting Data
# Inserting record one by one
query = db.insert(emp).values(Id=1, name='naveen', salary=60000.00, active=True) 
ResultProxy = connection.execute(query)

#Inserting many records at ones
query = db.insert(emp) 
values_list = [{'Id':'2', 'name':'ram', 'salary':80000, 'active':False},
               {'Id':'3', 'name':'ramesh', 'salary':70000, 'active':True}]
ResultProxy = connection.execute(query,values_list)

results = connection.execute(db.select([emp])).fetchall()
df = pd.DataFrame(results)
df.columns = results[0].keys()
df.head(4)


# ** with Large Dataset ** #
while flag:
    partial_results = ResultProxy.fetchmany(50)
    if(partial_results == []): 
	flag = False
    //
	code
   //
ResultProxy.close()


# ** convert dataframe ** #
df = pd.DataFrame(ResultSet)
df.columns = ResultSet[0].keys()
```
### Updating
``` python
# UPDATING DATABASES
# db.update(table_name).values(attribute = new_value).where(condition)
import sqlalchemy as db
import pandas as pd

engine = db.create_engine('sqlite:///test.sqlite')
metadata = db.MetaData()
connection = engine.connect()
emp = db.Table('emp', metadata, autoload=True, autoload_with=engine)

results = connection.execute(db.select([emp])).fetchall()
df = pd.DataFrame(results)
df.columns = results[0].keys()
df.head(4)
```

# example
import sqlalchemy as db
import pandas as pd

engine = db.create_engine('sqlite:///census.sqlite')
connection = engine.connect()
metadata = db.MetaData()

census = db.Table('census', metadata, autoload=True, autoload_with=engine)
state_fact = db.Table('state_fact', metadata, autoload=True, autoload_with=engine)

# Automatic Join
query = db.select([census.columns.pop2008, state_fact.columns.abbreviation])
result = connection.execute(query).fetchall()
df = pd.DataFrame(results)
df.columns = results[0].keys()
df.head(5)

# Manual Join
query = db.select([census, state_fact])
query = query.select_from(census.join(state_fact, census.columns.state == state_fact.columns.name))
results = connection.execute(query).fetchall()
df = pd.DataFrame(results)
df.columns = results[0].keys()
df.head(5)


# Build a statement to update the salary to 100000
query = db.update(emp).values(salary = 100000)
query = query.where(emp.columns.Id == 1)
results = connection.execute(query)

results = connection.execute(db.select([emp])).fetchall()
df = pd.DataFrame(results)
df.columns = results[0].keys()
df.head(4)


# **** DELETING A TABLE **** #

# db.delete(table_name).where(condition)

import sqlalchemy as db
import pandas as pd

engine = db.create_engine('sqlite:///test.sqlite')
metadata = db.MetaData()
connection = engine.connect()
emp = db.Table('emp', metadata, autoload=True, autoload_with=engine)

results = connection.execute(db.select([emp])).fetchall()
df = pd.DataFrame(results)
df.columns = results[0].keys()
df.head(4)

# Build a statement to delete where salary < 100000
query = db.delete(emp)
query = query.where(emp.columns.salary < 100000)
results = connection.execute(query)

results = connection.execute(db.select([emp])).fetchall()
df = pd.DataFrame(results)
df.columns = results[0].keys()
df.head(4)


# **** DROPPING A TABLE **** #

table_name.drop(engine) #drops a single table
metadata.drop_all(engine) #drops all the tables in the database
