# Chapter 5: Working with Databases in Python

# Relational Databases Principals

Relational databases are a type of database that follows a particular data model. The data is stored in tables, and each table has columns and rows, where columns represent the attribute of the data, and rows represent the instances of the data. 

The following are some of the basic principals of relational databases:

## 1. Tables

Tables are the basic building blocks of a relational database. Each table has a unique name and consists of rows and columns. The columns represent the attributes of the data, and the rows represent the data itself.

For example, consider a table called `customers` that stores information about the customers of a business. The columns of this table might include `customer_id`, `customer_name`, `customer_email`, and `customer_phone_number`. Each row in this table would represent a specific customer and contain values for each of the columns.

## 2. Keys

Keys are used to uniquely identify each row in a table. A primary key is a special type of key that uniquely identifies each row in a table. It must have a unique value for each row and cannot be null. 

For example, in the `customers` table mentioned earlier, the `customer_id` column might be designated as the primary key.

## 3. Relationships

Relationships are used to connect tables in a relational database. This allows data to be split into multiple tables while still maintaining the ability to retrieve and combine the data as needed.

For example, consider a second table called `orders` that stores information about orders placed by customers. This table might include columns such as `order_id`, `order_date`, and `customer_id`. The `customer_id` column in the `orders` table is a foreign key that references the `customer_id` column in the `customers` table. This allows us to connect orders to customers and retrieve data from both tables as needed.

## 4. Normalization

Normalization is the process of organizing data in a database to reduce redundancy and dependency. This helps to ensure data consistency and accuracy.

For example, consider a table that stores information about customers and their orders. If we store the customer's name and address in both the `customers` and `orders` tables, we introduce redundancy. Instead, we could create a separate table called `addresses` that stores the customer's address and link it to both the `customers` and `orders` tables using foreign keys. This eliminates redundancy and ensures that changes to a customer's address are made in only one place. 

By understanding these basic principals, we can begin to design and work with efficient, scalable, and maintainable relational databases in Python.# Chapter 5: Working with Databases in Python

# Connecting to Databases

To work with a database in Python, you first need to establish a connection to it. There are several libraries available in Python to connect to different types of databases, including MySQL, PostgreSQL, SQLite, and Oracle.

One of the most popular libraries for connecting to databases in Python is the `sqlite3` module, which comes with Python's standard library. Let's take a look at an example of how to connect to an SQLite database:

```python
import sqlite3

conn = sqlite3.connect('example.db')
```

In this example, we first import the `sqlite3` module. Then, we use the `connect()` function to create a connection object and connect to an SQLite database named `example.db`, which is located in the current working directory.

If you're connecting to a remote database, you'll need to specify the hostname, port number, database name, username, and password. For example, to connect to a MySQL database, you would use the `pymysql` library like this:

```python
import pymysql

conn = pymysql.connect(
    host='localhost',
    user='username',
    password='password',
    database='example_db',
    port=3306
)
```

In this example, we import the `pymysql` library and create a connection object to a MySQL database named `example_db` running on the localhost. We also specify the username, password, and port number.

It's important to note that when you're done working with a database, you should always close the connection to avoid leaving any resources open. You can do this by calling the `close()` method on the connection object:

```python
conn.close()
```

Now that we know how to establish a connection to a database, let's move on to learning how to query the database.

# Database Queries

Once a connection is established, we can begin querying the database. A query is a request for data or information from a database table or combination of tables. In Python, we can perform queries using SQL (Structured Query Language), which is a standard language used to communicate with databases.

Here is an example of a simple query to retrieve all the records from a table:

```python
import sqlite3

connection = sqlite3.connect('mydatabase.db')
cursor = connection.cursor()

query = "SELECT * FROM mytable"
cursor.execute(query)

rows = cursor.fetchall()

for row in rows:
    print(row)
```

In the example above, we use the `SELECT` statement to retrieve all the records from the `mytable` table. The `*` operator means that we want to retrieve all the columns in the table.

We then execute the query using the cursor's `execute()` method, and retrieve the results using the `fetchall()` method. The results are returned as a list of tuples, where each tuple represents a row in the table.

We can also use the `WHERE` clause to filter the results based on a condition. Here's an example:

```python
query = "SELECT * FROM mytable WHERE age > 18"
cursor.execute(query)

rows = cursor.fetchall()

for row in rows:
    print(row)
```

In the example above, we use the `WHERE` clause to retrieve only the records where the `age` column is greater than 18.

We can also use other SQL statements such as `INSERT`, `UPDATE`, and `DELETE` to modify the data in the database. Here's an example of an `INSERT` statement:

```python
query = "INSERT INTO mytable (name, age) VALUES ('John', 30)"
cursor.execute(query)

connection.commit()
```

In the example above, we use the `INSERT INTO` statement to add a new record to the `mytable` table. The values for the `name` and `age` columns are specified using the `VALUES` keyword.

After executing the query, we call the `commit()` method to save the changes to the database.

Overall, querying a database using Python is a powerful tool for managing data within applications. By using SQL statements, we can easily retrieve and modify data from a variety of databases.

# Data Management using ORM

Object-Relational Mapping (ORM) is a technique to map data between relational databases and the object-oriented programming language. It is a powerful tool that eliminates the need for writing complex SQL queries and provides a more intuitive way to interact with databases.

ORM is a framework that enables developers to interact with the database using high-level APIs. The ORM framework maps the database schema to the object model, which allows developers to manipulate the data using objects and methods instead of writing SQL queries. 

Python has popular ORM frameworks like Django ORM, SQLAlchemy, and Peewee. In this section, we'll use SQLAlchemy ORM to manage data in Python.

## SQLAlchemy ORM

SQLAlchemy is a popular Python ORM toolkit that provides a set of high-level APIs to interact with databases. It supports various database systems like SQLite, PostgreSQL, MySQL, and Oracle.

### Installation

You can install SQLAlchemy using pip:

```python
pip install SQLAlchemy
```

### Connecting to a Database

To connect to a database, we use the `create_engine()` function from SQLAlchemy. The function takes a database URL as a parameter.

```python
from sqlalchemy import create_engine

db_url = "postgresql://username:password@localhost/mydatabase"
engine = create_engine(db_url)
```

Here, we connect to a PostgreSQL database with the username `username`, password `password`, and database name `mydatabase`. You can replace the URL with your database URL.

### Defining a Model

To interact with a database using ORM, we need to define a model that represents the database table. The model is a Python class that inherits from the `Base` class of SQLAlchemy.

```python
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
```

Here, we define a model for a `books` table that has three columns: `id`, `title`, and `author`. The `__tablename__` attribute specifies the table name.

### Creating a Table

To create a table in the database, we use the `create_all()` method of the `Base` object.

```python
Base.metadata.create_all(engine)
```

This will create a `books` table in the database.

### Adding Data

To add data to the database, we create an instance of the model and add it to the session.

```python
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

book1 = Book(title='The Alchemist', author='Paulo Coelho')
book2 = Book(title='The Great Gatsby', author='F. Scott Fitzgerald')

session.add(book1)
session.add(book2)

session.commit()
```

Here, we create two `Book` objects and add them to the session using the `add()` method. Finally, we commit the changes to the database using the `commit()` method.

### Querying Data

To query data from the database, we use the `query()` method of the session object.

```python
books = session.query(Book).all()

for book in books:
    print(book.title, book.author)
```

This will print the titles and authors of all the books in the database.

### Updating Data

To update data in the database, we modify the object attributes and commit the changes to the session.

```python
book = session.query(Book).filter_by(title='The Alchemist').first()
book.author = 'Paulo Coelho (Updated)'

session.commit()
```

Here, we get a `Book` object with the specified title using the `filter_by()` method and modify the author attribute. Finally, we commit the changes to the database.

### Deleting Data

To delete data from the database, we get the object to be deleted and call the `delete()` method on it.

```python
book = session.query(Book).filter_by(title='The Great Gatsby').first()
session.delete(book)

session.commit()
```

This will delete the `Book` object with the specified title from the database.

## Conclusion

ORM is a powerful tool that provides an intuitive way to interact with databases. SQLAlchemy is a popular ORM framework for Python that provides a set of high-level APIs to manage data in databases. With SQLAlchemy ORM, you can create models that represent database tables, add data, query data, update data, and delete data using high-level APIs.