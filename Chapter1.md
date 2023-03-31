# Chapter 1: Python Basics

## Introduction to Python

Python is a high-level, interpreted programming language that is widely used for general-purpose programming. It was created in the late 1980s by Guido van Rossum.

Python is known for its simplicity, ease of use, and readability, which makes it a popular choice for beginners learning to code. Its syntax is easy to understand and requires fewer lines of code compared to other programming languages.

Python can be used for a variety of applications, including web development, data analysis, artificial intelligence, machine learning, and scientific computing.

Some of the features that make Python popular among developers are:

- **Interpreted**: Python code is interpreted line by line, which makes it easy to test and debug.
- **Object-oriented**: Python supports object-oriented programming principles, which makes it easy to write reusable and maintainable code.
- **High-level**: Python provides high-level data structures and abstractions, which makes it easy to write complex programs quickly.
- **Dynamic**: Python is a dynamically-typed language, which means that you don't have to declare the data type of a variable before using it.
- **Extensible**: Python can be extended using C or C++ code, which makes it a versatile language.

Python is an open-source language, which means that it is free to use and distribute. It has a large and active community of developers, who contribute to its development and provide support to other developers.

Here's an example of a "Hello, World!" program in Python:

```python
print("Hello, World!")
```

This program prints the message "Hello, World!" to the console. As you can see, the syntax is straightforward, and the program requires only one line of code.# [Chapter 1: Python Basics](chapter1_0.1.md)

# Installation and Setup

Python is available for different platforms such as Windows, macOS, and Linux. The latest version can be downloaded from the official website [https://www.python.org/downloads/](https://www.python.org/downloads/). 

## Windows

To install Python on Windows, follow these steps:

1. Download the latest version of Python from [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/).
2. Double-click on the downloaded file to start the installation process.
3. Select the option to add Python to the PATH environment variable.
4. Follow the instructions in the installation wizard to complete the installation.

Once the installation is complete, you can open a Command Prompt window and type `python` to start the Python interpreter.

## macOS

macOS comes with a pre-installed version of Python. However, you can install the latest version using Homebrew, a popular package manager for macOS.

1. Open Terminal from the Applications/Utilities folder.
2. Install Homebrew by running the following command:

    ```
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
    ```

3. Install Python using Homebrew by running the following command:

    ```
    brew install python
    ```

4. Once the installation is complete, you can open a Terminal window and type `python3` to start the Python interpreter.

## Linux

Python is available in most Linux distributions. You can install it using the package manager of your distribution. For example, in Ubuntu, you can install Python using the following command:

```
sudo apt-get install python3
```

Once the installation is complete, you can open a Terminal window and type `python3` to start the Python interpreter.# [Chapter 1: Python Basics](chapter1_0.1.md)

## Running Python Code

After installing Python, we can run Python code in different ways. The most common ways are:

### 1. Using Python Interpreter

We can run Python code by invoking the Python interpreter from the command line. Open the terminal or command prompt and type `python`. It will show the Python version and `>>>` prompt for input. We can type our Python code line by line and press enter to execute. Here is an example:

```python
$ python
Python 3.8.0 (default, Nov  4 2019, 15:23:05)
[GCC 7.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Hello World")
Hello World
```

To exit the interpreter type `exit()` or press `CTRL-D`.

### 2. Running Python File

We can also run Python code by saving it in a file with `.py` extension and running it with the Python interpreter. Here is an example:

```python
# File: hello.py
print("Hello World")
```

In the terminal or command prompt, navigate to the directory where the `hello.py` file is saved and type `python hello.py`. It will execute the code and produce the output.

```python
$ python hello.py
Hello World
```

### 3. Integrated Development Environment (IDE)

We can use an IDE to write Python code and run it within the same application. There are many IDEs available for Python development such as PyCharm, Visual Studio Code, Spyder, and IDLE. IDEs provide features such as code highlighting, debugging, code completion, and more.

Using an IDE can make the development process faster and more efficient. Here is an example of running Python code using PyCharm:

```python
# File: hello.py
print("Hello World")
```

Open PyCharm and create a new project. Create a new file called `hello.py` and paste the above code. Press `CTRL-SHIFT-F10` or right-click on the file and select `Run hello`. It will execute the code and produce the output.

```python
Hello World
```

In this chapter, we have seen how to run Python code using different methods. It is important to choose the method that suits our needs and preferences.# [Chapter 1: Python Basics](chapter1_0.1.md)

# Basic Syntax

The syntax of the Python programming language is simple and easy to learn. It is designed to be readable and intuitive, making it popular among beginners and experts alike. Here are some basic syntax rules to keep in mind when writing Python code:

## Statements

A statement is a single line of code that performs a specific action, such as assigning a value to a variable or printing a message to the console. In Python, statements are typically written on separate lines, and the end of a statement is marked by a newline character. 

```python
# Assigning a value to a variable
x = 10

# Printing a message to the console
print("Hello, World!")
```

## Indentation

Python uses indentation to indicate the scope of a block of code, such as a function, loop, or conditional statement. Instead of using curly braces like many other programming languages, Python relies on consistent indentation to make the code easier to read and understand.

```python
# Example of indentation in a function definition
def my_function():
    if x > 10:
        print("x is greater than 10")
    else:
        print("x is less than or equal to 10")
```

## Comments

Comments are used to add explanatory notes or documentation to your code. In Python, comments begin with the hash symbol (`#`) and continue to the end of the line. 

```python
# This is a comment
# It explains what the next line of code does
x = 10  # Assigning the value 10 to the variable x
```

## Semicolons

In Python, semicolons are used to separate multiple statements on a single line. While it is possible to write code in this way, it is generally not recommended, as it can make the code harder to read and understand.

```python
# Example of using semicolons to separate statements
x = 10; y = 20; z = x + y
```

## Keywords

Python has a set of reserved keywords that have special meanings and cannot be used as variable names or other identifiers. Here are some examples of Python keywords:

```python
# Example of some Python keywords
if, else, elif, while, for, break, continue, def, return, import, from, in, not, and, or, True, False, None
```

Understanding these basic syntax rules is critical to writing Python code that is effective, efficient, and easy to read and understand.# [Chapter 1: Python Basics](chapter1_0.1.md)

# Variables and Data Types

Variables are used to store data in a program. In Python, you do not need to declare the type of the variable before assigning a value to it. Python automatically determines the data type based on the value assigned to the variable.

## Data Types in Python

Python has several built-in data types, which include:

### Numeric types
- int (integer)
- float (floating-point number)
- complex (complex number)

### Sequences
- str (string)
- list
- tuple
- range

### Sets and Dictionaries
- set
- frozenset
- dict

### Boolean type
- bool (Boolean: True or False)

### NoneType
- None (special object indicating the absence of a value)

Here are some examples of assigning values to variables:

```python
# Integer
age = 25

# Float
salary = 2500.50

# String
name = "John Doe"

# List
fruits = ['apple', 'banana', 'cherry']

# Tuple
coordinates = (10, 20)

# Set
numbers = {1, 2, 3, 4, 5}

# Dictionary
person = {'name': 'John', 'age': 25, 'city': 'New York'}

# Boolean
is_valid = True

# NoneType
value = None
```

You can also use the `type()` function to check the data type of a variable:

```python
age = 25
print(type(age))  # Output: <class 'int'>

salary = 2500.50
print(type(salary))  # Output: <class 'float'>

name = "John Doe"
print(type(name))  # Output: <class 'str'>
```

In Python, variables are case-sensitive, which means that `age`, `Age`, and `AGE` are three different variables.

## Variable Naming Rules

When naming variables, you must follow some rules:

- The name can only contain letters (a to z, A to Z), digits (0 to 9), and underscores (_).
- The name must start with a letter or an underscore.
- The name cannot start with a digit.
- Variable names are case-sensitive.

Here are some valid variable names:

```python
name = "John"
age = 25
salary_2020 = 50000.00
```

And here are some invalid variable names:

```python
2name = "John"  # Invalid: Cannot start with a digit
name@ = "John"  # Invalid: Contains an invalid character
```

It is also good practice to use descriptive variable names that reflect the data they store. This makes your code more readable and easier to maintain.# [Chapter 1: Python Basics](chapter1_0.1.md)

## Control Statements

Control statements in Python are used to control the flow of execution of a program based on certain conditions. The three main control statements in Python are if-else statements, for loops, and while loops.

### If-else Statements

If-else statements are used to execute a block of code if a certain condition is met or to execute a different block of code if the condition is not met. The syntax of an if-else statement is as follows:

```python
if condition:
    # code to be executed if condition is true
else:
    # code to be executed if condition is false
```

Here's an example:

```python
x = 5

if x > 10:
    print("x is greater than 10")
else:
    print("x is less than or equal to 10")
```

In this example, since x is less than or equal to 10, the output will be:

```
x is less than or equal to 10
```

### For Loops

For loops are used to iterate over a sequence of elements, such as a list or a string. The syntax of a for loop is as follows:

```python
for variable in sequence:
    # code to be executed for each element in the sequence
```

Here's an example:

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

In this example, the output will be:

```
apple
banana
cherry
```

### While Loops

While loops are used to repeatedly execute a block of code as long as a certain condition is true. The syntax of a while loop is as follows:

```python
while condition:
    # code to be executed while condition is true
```

Here's an example:

```python
i = 1

while i <= 5:
    print(i)
    i += 1
```

In this example, the output will be:

```
1
2
3
4
5
```# [Chapter 1: Python Basics](chapter1_0.1.md)

# Functions

Functions are blocks of code that perform specific tasks. They are reusable and modular, making them an essential part of any programming language. Functions help break down complex programs into smaller, more manageable pieces of code. 

To define a function in Python, we use the `def` keyword followed by the function name, parameters (if any), and a colon `:`. The function code is then indented below the function definition.

Here is an example of a simple function that adds two numbers together:

```python
def add_numbers(num1, num2):
    sum = num1 + num2
    return sum
```

In this example, the function `add_numbers()` takes two parameters `num1` and `num2`. It then adds them together and returns the result using the `return` keyword. 

We can call the `add_numbers()` function as follows:

```python
result = add_numbers(10, 20)
print(result)
```

This will output `30`, which is the sum of `10` and `20`.

Python functions can have any number of parameters, including optional ones. Here is an example of a function that takes one required parameter and one optional parameter:

```python
def greet(name, message = "Hello"):
    print(message + ", " + name)

greet("John")        # Output: Hello, John
greet("Jane", "Hi")  # Output: Hi, Jane
```

In this example, the `greet()` function takes two parameters: `name` and `message` (with a default value of `"Hello"`). The function then prints the message followed by the name.

We can call the `greet()` function with a single argument (`name`), and it will use the default message `"Hello"`. Or we can pass both `name` and `message` as arguments.

Functions can also return multiple values using tuples. Here is an example:

```python
def square_and_cube(num):
    square = num ** 2
    cube = num ** 3
    return square, cube

s, c = square_and_cube(3)
print(s, c)   # Output: 9 27
```

In this example, the `square_and_cube()` function takes one parameter `num` and calculates its square and cube. The values are then returned as a tuple. We can then use tuple unpacking to assign the two values to variables `s` and `c`.

Functions can be defined anywhere in the code, even inside other functions. We can also call a function recursively (a function that calls itself) to solve certain problems. 

In conclusion, functions are essential building blocks of any programming language, and Python is no exception. They help us break down complex programs into smaller, more manageable pieces of code.# [Chapter 1: Python Basics](chapter1_0.1.md)

# Modules

Python modules are files containing Python definitions and statements. A Python module can define functions, classes, and variables. A module can also include runnable code.

## Importing Modules

To use the definitions in a module, you need to import the module first. There are several ways to import a module:

### Import the entire module

```python
import math
```

This imports the entire math module. You can now access any function or variable defined in the math module using the `math.` prefix, for example:

```python
print(math.pi)  # Output: 3.141592653589793
```

### Import a specific function or variable from a module

```python
from math import pi
```

This imports only the `pi` variable from the math module. You can now use `pi` directly without the `math.` prefix:

```python
print(pi)  # Output: 3.141592653589793
```

### Import multiple functions or variables from a module

```python
from math import pi, sqrt
```

This imports both the `pi` and `sqrt` functions from the math module. You can now use them directly without the `math.` prefix:

```python
print(sqrt(4))  # Output: 2.0
```

### Import a module with an alias

```python
import math as m
```

This imports the math module with the alias `m`. You can now access any function or variable defined in the math module using the `m.` prefix:

```python
print(m.pi)  # Output: 3.141592653589793
```

## Creating Modules

You can create your own modules in Python by saving a Python file with the `.py` extension. For example, let's create a module called `my_module.py` with the following code:

```python
def say_hello(name):
    print(f"Hello, {name}!")

def calculate_sum(a, b):
    return a + b
```

To use the functions in `my_module.py`, you need to import the module first:

```python
import my_module

my_module.say_hello("Alice")  # Output: "Hello, Alice!"
print(my_module.calculate_sum(2, 3))  # Output: 5
```

You can also import specific functions from `my_module.py`:

```python
from my_module import say_hello

say_hello("Bob")  # Output: "Hello, Bob!"
```

## Conclusion

Modules are an essential part of Python programming. They allow you to organize your code into reusable, sharable, and extensible components. By using modules, you can write more efficient and maintainable code.# [Chapter 1: Python Basics](chapter1_0.1.md)

# Exceptions Handling

In Python, an exception is a type of error that occurs during the execution of a program. When an error occurs, Python generates an exception which can be handled by the program to prevent it from crashing. Python provides a robust exception handling mechanism, which allows the programmer to handle these exceptions gracefully.

## Handling Exceptions

In Python, exceptions are handled using the `try` and `except` statements. The `try` statement is used to enclose the code that might raise an exception, while the `except` statement is used to handle the exception.

Here's the basic syntax of a try-except block:

```python
try:
    # code that may raise an exception
except ExceptionType:
    # code to handle the exception
```

For example, let's say we have a function that divides two numbers:

```python
def divide(x, y):
    return x / y
```

If we call this function with the wrong arguments, i.e., the second argument is zero, it will raise a `ZeroDivisionError` exception.

```python
>>> divide(10, 0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in divide
ZeroDivisionError: division by zero
```

To handle this exception, we can enclose the function call in a `try` block and handle the exception in an `except` block:

```python
try:
    result = divide(10, 0)
except ZeroDivisionError:
    print("Error: division by zero")
```

Now if we run this code, it will not crash, and we will get a helpful error message instead:

```python
Error: division by zero
```

## Catching Multiple Exceptions

It's possible to handle multiple exceptions using a single `try` statement. The `except` statement can be followed by a tuple of exception types to catch.

```python
try:
    # code that may raise an exception
except (ExceptionType1, ExceptionType2, ...):
    # code to handle the exception
```

For example, let's say we have a function that reads a file and returns its contents:

```python
def read_file(filename):
    file = open(filename, "r")
    contents = file.read()
    file.close()
    return contents
```

If the specified file doesn't exist, the `open()` function will raise a `FileNotFoundError` exception. If there's a problem with reading the file, the `read()` function will raise an `IOError` exception.

To handle both of these exceptions, we can enclose the function call in a `try` block and catch both exceptions in an `except` block:

```python
try:
    contents = read_file("nonexistent_file.txt")
except (FileNotFoundError, IOError):
    print("Error: could not read file")
```

Now if we run this code, it will not crash, and we will get a helpful error message instead:

```python
Error: could not read file
```

## Finally Block

In some cases, you might want to execute a block of code after a `try` block, regardless of whether an exception was raised or not. For example, you might want to close a file handle or release a network connection.

To do this, you can use a `finally` block. The code inside the `finally` block will always execute, even if an exception is raised.

Here's an example:

```python
try:
    # code that may raise an exception
finally:
    # code to execute regardless of whether an exception was raised or not
```

For example, let's say we have a function that opens a file, reads its contents, and then closes the file handle:

```python
def read_file(filename):
    file = open(filename, "r")
    try:
        contents = file.read()
    finally:
        file.close()
    return contents
```

Now if we call this function and an exception is raised, the file handle will still be closed:

```python
>>> read_file("nonexistent_file.txt")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 4, in read_file
FileNotFoundError: [Errno 2] No such file or directory: 'nonexistent_file.txt'
```

## Raising Exceptions

In addition to handling exceptions, Python also allows you to raise exceptions explicitly using the `raise` statement. 

Here's an example of how to raise an exception:

```python
raise ExceptionType("Error message")
```

For example, let's say we have a function that checks if a number is negative. If the number is negative, we want to raise a `ValueError` exception.

```python
def check_positive(number):
    if number < 0:
        raise ValueError("Number must be positive")
```

Now if we call this function with a negative number, it will raise a `ValueError`:

```python
>>> check_positive(-1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in check_positive
ValueError: Number must be positive
```