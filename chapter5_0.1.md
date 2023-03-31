# Relational Databases Principles

A relational database is a type of database that organizes data into one or more tables with a unique key identifying each row. Each table is made up of columns (also called attributes) and rows (also called tuples or records). The columns represent the data attributes, while the rows represent the data itself. 

The main principles of a relational database include:

### 1. Data Integrity

Data integrity ensures that the data stored in the database is accurate and consistent. It is enforced through the use of constraints, which define rules that the data must follow. For example, a constraint may require that a specific column cannot have null values or that every row must have a unique value for a certain column.

### 2. Data Consistency

Data consistency ensures that the data is reliable and can be trusted. This is achieved through the use of constraints and relationships between tables. For example, a relationship between two tables ensures that a value in one table is related to a value in another table, and that the relationship is maintained when data is added, modified, or deleted.

### 3. Data Normalization

Data normalization is the process of organizing data in a way that reduces redundancy and improves data integrity. It involves breaking down large tables into smaller, more specialized tables, and establishing relationships between them. For example, instead of having one large table with all customer information, you could have separate tables for customers, orders, and products, and establish relationships between them.

### 4. Data Security

Data security ensures that the data is protected from unauthorized access, modification, or deletion. This is achieved through the use of authentication, access control, and encryption. For example, you may require users to log in with a username and password, and restrict access to certain tables or columns based on their role or permissions.

By understanding these principles, you can design and implement a relational database that is efficient, reliable, and secure.# Connecting to Databases

In order to interact with a database, you first need to establish a connection. This connection serves as a bridge between your Python code and the database.

To connect to a database, you need to provide the following information:

- Hostname or IP address of the machine where the database is running
- Port number on which the database is listening (usually 5432 for PostgreSQL and 3306 for MySQL)
- Database name
- Credentials (username and password) for accessing the database

Here's an example of how to connect to a PostgreSQL database using the `psycopg2` library:

```python
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="mydatabase",
    user="myusername",
    password="mypassword"
)
```

And here's an example of how to connect to a MySQL database using the `mysql-connector-python` library:

```python
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="mydatabase",
    user="myusername",
    password="mypassword"
)
```

Once you have established a connection, you can perform various operations such as creating tables, inserting data, updating data, deleting data, and fetching data. We will cover these operations in more detail in later sections.# Database Queries

Once you have connected to a database using Python, you can start querying the database to retrieve information. In a relational database, information is stored in tables, and you can use SQL (Structured Query Language) to extract information from the tables.

In Python, you can use a variety of libraries to interact with databases and execute SQL statements. The most commonly used libraries are `sqlite3`, `mysql-connector-python`, `psycopg2`, `pyodbc`, and `sqlalchemy`.

For example, if you're using `sqlite3` and you want to retrieve all the information from a table named `employees`, you can execute the following SQL statement:

```python
import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()

c.execute('SELECT * FROM employees')
data = c.fetchall()

print(data)
```

In this example, we first establish a connection to the database by creating a `Connection` object using the `connect()` method. We then create a `Cursor` object, which allows us to execute SQL statements against the database. We execute the SQL statement `SELECT * FROM employees`, which retrieves all the data from the `employees` table. Finally, we use the `fetchall()` method to retrieve all the rows returned by the query.

If you want to retrieve only a subset of the data, you can use the `WHERE` clause to filter the results. For example, if you want to retrieve all the employees whose last name is `Smith`, you can execute the following SQL statement:

```python
c.execute('SELECT * FROM employees WHERE last_name = "Smith"')
data = c.fetchall()

print(data)
```

In this example, we added the `WHERE` clause to the SQL statement to filter the results. The `=` operator is used to compare the `last_name` column in the `employees` table with the string `"Smith"`. The result is a list of all the employees whose last name is `"Smith"`.

You can also use the `ORDER BY` clause to sort the results. For example, if you want to retrieve all the employees from the `employees` table in alphabetical order by their last name, you can execute the following SQL statement:

```python
c.execute('SELECT * FROM employees ORDER BY last_name')
data = c.fetchall()

print(data)
```

In this example, we added the `ORDER BY` clause to the SQL statement to sort the results by the `last_name` column in ascending order.

These are just a few examples of how you can use SQL to retrieve data from a database using Python. With these tools, you can easily manipulate the data and perform complex queries to extract the information you need.# Data management using ORM

ORM stands for Object-Relational Mapping, which is a technique used to connect object-oriented programming languages with relational databases. Python has several ORM libraries, including SQLAlchemy, Django ORM, and Peewee, to name a few.

ORM libraries provide a way to work with databases using object-oriented programming concepts such as classes and objects instead of writing complex SQL queries. This approach helps developers to write cleaner and more modular code.

Here's an example of how SQLAlchemy ORM can be used to interact with a database:

```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///example.db', echo=True)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)

Session = sessionmaker(bind=engine)
session = Session()

new_user = User(username='john', password='doe')
session.add(new_user)
session.commit()

user = session.query(User).filter_by(username='john').first()
print(user.id, user.username, user.password)
```

In the example above, we create a connection to a SQLite database using SQLAlchemy's `create_engine()` function. Then, we define a User class that inherits from the declarative_base() class provided by SQLAlchemy. The User class is mapped to a database table called `users` using the `__tablename__` attribute.

The `id`, `username`, and `password` attributes of the User class are mapped to the corresponding columns in the `users` table. We create a session using the `sessionmaker()` function, which provides a high-level API for interacting with the database.

We create a new user object and add it to the session using `session.add()`, then commit the changes to the database using `session.commit()`. Finally, we query the database for the user with the username `john` using `session.query()` and the `filter_by()` method, and print out the results.

ORM libraries can also help with data validation and input sanitization, making it easier to build secure and scalable applications. By using ORM libraries, developers can focus on the business logic of their application without worrying too much about the underlying database.