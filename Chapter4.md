# Chapter 4: File Handling in Python

# Reading and Writing Files

Python provides a simple and easy-to-use way to work with files. In this section, we'll learn how to read and write files in Python.

## Reading Files

To read a file in Python, we first need to open it using the `open()` function. The `open()` function takes two arguments: the name of the file we want to open and the mode in which we want to open it. The mode can be either `r` (read mode), `w` (write mode), or `a` (append mode).

```python
# Read mode
file = open("example.txt", "r")

# Read the contents of the file
content = file.read()

# Close the file
file.close()
```

In the above example, we opened the file "example.txt" in read mode using the `open()` function. We then read the contents of the file using the `read()` method and stored it in the `content` variable. Finally, we closed the file using the `close()` method.

## Writing Files

To write to a file in Python, we also need to use the `open()` function. However, this time we need to specify the mode as `w` (write mode).

```python
# Write mode
file = open("example.txt", "w")

# Write some text to the file
file.write("Hello, world!")

# Close the file
file.close()
```

In the above example, we opened the file "example.txt" in write mode using the `open()` function. We then wrote the text "Hello, world!" to the file using the `write()` method. Finally, we closed the file using the `close()` method.

## Text vs Binary Mode

When working with files, we need to specify whether we want to work with them in text mode or binary mode. By default, files are opened in text mode.

Text mode is used when working with plain text files such as `.txt` files. In text mode, the data is encoded as Unicode.

Binary mode is used when working with non-text files such as images or audio files. In binary mode, the data is not encoded as Unicode.

To specify which mode we want to work with, we need to add a `t` or `b` to the mode string.

```python
# Text mode
file = open("example.txt", "rt")

# Binary mode
file = open("example.bin", "rb")
```

## CSV and JSON Files

CSV and JSON are popular file formats used for storing structured data. Python provides built-in support for working with these file formats.

To read a CSV file in Python, we can use the `csv` module.

```python
import csv

# Read a CSV file
with open("example.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

In the above example, we read the contents of a CSV file "example.csv" using the `csv` module. We then used a `for` loop to iterate over each row in the file and printed it to the console.

To read a JSON file in Python, we can use the `json` module.

```python
import json

# Read a JSON file
with open("example.json", "r") as file:
    data = json.load(file)
    print(data)
```

In the above example, we read the contents of a JSON file "example.json" using the `json` module. We then used the `load()` method to load the contents of the file into a Python dictionary and printed it to the console.

## Error Handling

When working with files, it's important to handle errors that may occur. For example, if we try to open a file that doesn't exist, Python will raise a `FileNotFoundError`. We can handle this error using a `try`-`except` block.

```python
try:
    file = open("example.txt", "r")
except FileNotFoundError:
    print("File not found.")
else:
    content = file.read()
    file.close()
```

In the above example, we use a `try`-`except` block to handle the `FileNotFoundError` that may occur if the file "example.txt" doesn't exist. If the file exists, we read its contents and close it. If it doesn't exist, we print an error message to the console.# Chapter 4: File Handling in Python

## Text vs Binary Mode

When working with files in Python, one of the first decisions to make is whether to open the file in text mode or binary mode. 

### Text Mode

In text mode, data is treated as a sequence of characters. This is useful when working with files that contain human-readable text. For example, if we have a file called `example.txt` that contains the following text:

```
Hello, world!
```

We can read this file in text mode as follows:

```python
with open('example.txt', 'r') as f:
    contents = f.read()
    
print(contents)  # Output: 'Hello, world!\n'
```

We can also write text to a file in text mode:

```python
with open('example.txt', 'w') as f:
    f.write('Goodbye, world!')
```

This will overwrite the contents of `example.txt` with the string "Goodbye, world!".

### Binary Mode

In binary mode, data is treated as a sequence of bytes. This is useful when working with files that contain non-text data, such as images or audio. For example, if we have a file called `example.jpg` that contains an image, we can read this file in binary mode as follows:

```python
with open('example.jpg', 'rb') as f:
    contents = f.read()
```

Note the use of the `'rb'` mode string to open the file in binary mode. 

We can also write binary data to a file in binary mode:

```python
with open('example.jpg', 'wb') as f:
    f.write(binary_data)
```

Here, `binary_data` is a bytes object that contains the binary data we want to write to the file. 

### Conclusion

When working with files in Python, it's important to choose the correct mode for the data you're working with. Use text mode when working with human-readable text files, and binary mode when working with non-text data.# Chapter 4: File Handling in Python

## CSV and JSON Files

### CSV Files

Comma Separated Values (CSV) is a popular file format used to store and exchange data between applications. Each line in a CSV file represents a row in a table, and the values in each row are separated by commas. CSV files can be easily created and read using Python's built-in `csv` module.

Here is an example of how to read data from a CSV file:

```python
import csv

with open('example.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

This code will open the file `example.csv`, read its contents, and print each row to the console.

Similarly, you can write data to a CSV file using the `csv.writer` object:

```python
import csv

data = [
    ['Name', 'Age', 'Gender'], 
    ['John', '25', 'Male'], 
    ['Jane', '30', 'Female']
]

with open('example.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)
```

This code will create a new file called `example.csv` and write the data to it. The `newline` parameter is used to ensure that each row is written on a new line.

### JSON Files

JavaScript Object Notation (JSON) is a popular file format used to store and exchange data between applications. It is a text-based format that is easy to read and write, and can be used with many programming languages, including Python. JSON files can be easily created and read using Python's built-in `json` module.

Here is an example of how to read data from a JSON file:

```python
import json

with open('example.json', 'r') as f:
    data = json.load(f)
    print(data)
```

This code will open the file `example.json`, read its contents, and parse it into a Python dictionary. The dictionary can then be used to access the data in the file.

Similarly, you can write data to a JSON file using the `json.dump` method:

```python
import json

data = {
    'Name': 'John', 
    'Age': 25, 
    'Gender': 'Male'
}

with open('example.json', 'w') as f:
    json.dump(data, f)
```

This code will create a new file called `example.json` and write the data to it in JSON format.

### Error Handling

When working with files, it is important to handle errors that may occur. Common errors include file not found, permission denied, and invalid file format. Python provides several ways to handle errors when working with files.

Here is an example of how to handle file not found error using `try` and `except` statements:

```python
try:
    with open('example.txt', 'r') as f:
        data = f.read()
        print(data)
except FileNotFoundError:
    print('File not found.')
```

This code will attempt to open the file `example.txt` and read its contents. If the file is not found, an error message will be printed to the console.

Similarly, you can handle other types of errors using appropriate `try` and `except` statements. It is also recommended to use `finally` statement to close the file, regardless of whether an error occurred or not:

```python
try:
    with open('example.txt', 'r') as f:
        data = f.read()
        print(data)
except FileNotFoundError:
    print('File not found.')
except Exception as e:
    print('An error occurred:', str(e))
finally:
    f.close()
```

This code will handle both file not found and other types of errors, and will close the file in the `finally` block.# Chapter 4: File Handling in Python

## Error Handling

When working with files, errors can occur due to various reasons such as incorrect file path, file not found, insufficient permissions, or file already open by another process. To handle such errors appropriately and prevent program crashes, Python provides error handling mechanisms such as try-except blocks.

In file handling, errors can occur during file operations such as opening, reading, or writing to a file. Let's take a look at an example code that reads a file:

```python
try:
    with open('myfile.txt', 'r') as file:
        data = file.read()
except FileNotFoundError:
    print('File not found')
except IOError:
    print('Error reading file')
```

Here, we use a `try-except` block to handle two possible errors that can occur while reading the `myfile.txt` file. If the file is not found, the `FileNotFoundError` exception is raised and the message "File not found" is printed. If there is an error while reading the file, the `IOError` exception is raised and the message "Error reading file" is printed.

Similarly, we can use `try-except` blocks for handling errors while writing to a file. Let's consider an example that writes a list of strings to a file:

```python
strings = ['apple', 'banana', 'cherry']

try:
    with open('myfile.txt', 'w') as file:
        for string in strings:
            file.write(string + '\n')
except IOError:
    print('Error writing to file')
```

In this example, we use a `try-except` block to handle any errors that may occur while writing to the `myfile.txt` file. If there is an error while writing to the file, the `IOError` exception is raised and the message "Error writing to file" is printed.

Error handling is an essential part of file handling in Python. It helps prevent program crashes due to unexpected errors and provides a fallback mechanism to handle them gracefully.