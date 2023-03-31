# Reading and Writing Files

In Python, you can read and write data to files using the built-in `open()` function. This function takes two arguments: the file name/path and the mode in which the file should be opened. 

There are two modes in which a file can be opened: text mode and binary mode. In text mode, the file is opened as a string, while in binary mode, the file is opened as bytes.
```python
# Opening a file in text mode
file = open('example.txt', 'r')

# Opening a file in binary mode
file = open('example.bin', 'rb')
```
The `open()` function returns a file object that can be used to read from or write to the file.

## Reading Files
To read data from a file, you can use the `read()` method of the file object. This method reads the entire contents of the file as a string (in text mode) or as bytes (in binary mode).

```python
# Reading a file in text mode
with open('example.txt', 'r') as file:
    data = file.read()
    print(data)
    
# Reading a file in binary mode
with open('example.bin', 'rb') as file:
    data = file.read()
    print(data)
```
You can also read a file line by line using the `readline()` method. This method reads one line at a time and returns it as a string.

```python
# Reading a file line by line
with open('example.txt', 'r') as file:
    line = file.readline()
    while line:
        print(line)
        line = file.readline()
```

## Writing Files
To write data to a file, you can use the `write()` method of the file object. This method writes a string (in text mode) or bytes (in binary mode) to the file.

```python
# Writing to a file in text mode
with open('example.txt', 'w') as file:
    file.write('Hello, World!')
    
# Writing to a file in binary mode
with open('example.bin', 'wb') as file:
    data = b'\x48\x65\x6c\x6c\x6f\x2c\x20\x57\x6f\x72\x6c\x64\x21'
    file.write(data)
```

## Closing Files
It's important to close files once you're done with them to free up system resources. You can do this by calling the `close()` method of the file object.

```python
# Closing a file
file = open('example.txt', 'r')
data = file.read()
file.close()
```

## Error Handling
When working with files, you may encounter errors such as file not found or permission denied. To handle these errors, you can use a `try...except` block.

```python
try:
    with open('example.txt', 'r') as file:
        data = file.read()
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("Permission denied!")
``` 

## Conclusion
In Python, file handling is a fundamental concept. You can read and write data to files using the `open()` function and manipulate the data using the various methods provided by the file object. Don't forget to close the file once you're done with it, and always handle errors gracefully using a `try...except` block.# Text vs Binary Mode

When opening a file in Python, you have the option to open it in either **text** or **binary** mode. 

### Text Mode
Opening a file in text mode is the default mode. Text mode is used for handling files that contain text data, such as `.txt` files. In text mode, data is automatically decoded into strings when it is read from a file, and encoded back into bytes when it is written to a file.

```python
with open('example.txt', 'r') as f:
    data = f.read()
```

### Binary Mode
Binary mode should be used when handling files that contain non-text data, such as images or audio files. In binary mode, data is read and written as raw bytes. 

```python
with open('image.png', 'rb') as f:
    data = f.read()
```

When opening a file in binary mode, it is important to use the `'b'` character in the mode argument. This ensures that the file is being opened in binary mode.

```python
with open('image.png', 'r') as f: # this will raise an error, as we're trying to open a binary file in text mode
    data = f.read()
```

### Choosing the Right Mode
Choosing the right mode is important for ensuring that the data is being read and written correctly. If you're not sure which mode to use, check the documentation for the specific file format you're working with. 

In general, if you're working with files that contain text data, use text mode. If you're working with files that contain non-text data, use binary mode.# CSV and JSON Files

CSV (Comma Separated Values) and JSON (JavaScript Object Notation) are two popular file formats used for data exchange between systems. In Python, we have built-in libraries to handle both file formats.

## Reading CSV Files

To read a CSV file, we use the `csv` module. Here's an example:

```python
import csv

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

In the code above, we open the `data.csv` file in read mode and create a `csv.reader` object. We loop through each row of the file and print it to the console.

## Writing CSV Files

To write to a CSV file, we use the `csv.writer` object. Here's an example:

```python
import csv

data = [
    ['Name', 'Age', 'Country'],
    ['John', '25', 'USA'],
    ['Alice', '30', 'Canada'],
    ['Bob', '20', 'Mexico']
]

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
```

In the code above, we create a list of lists containing the data we want to write to the file. We open the `data.csv` file in write mode and create a `csv.writer` object. We then call `writerows` method to write the data to the file.

## Reading JSON Files

To read a JSON file, we use the `json` module. Here's an example:

```python
import json

with open('data.json', 'r') as file:
    data = json.load(file)
    print(data)
```

In the code above, we open the `data.json` file in read mode and use the `json.load` method to load the data into a Python object.

## Writing JSON Files

To write to a JSON file, we use the `json.dump` method. Here's an example:

```python
import json

data = {'Name': 'John', 'Age': 25, 'Country': 'USA'}

with open('data.json', 'w') as file:
    json.dump(data, file)
```

In the code above, we create a dictionary containing the data we want to write to the file. We open the `data.json` file in write mode and use the `json.dump` method to write the data to the file.

## Conclusion

CSV and JSON files are two widely used file formats for exchanging data between systems. Python's built-in libraries make it easy for us to read and write these files. When working with these files, it's important to handle errors gracefully using the error handling techniques we covered earlier in this chapter.## Error Handling

File handling in Python can be tricky business. One of the most important things to keep in mind is the proper handling of errors. When working with files, things can go wrong in many ways, such as file not found, read/write errors, and permissions issues.

To handle errors in Python, we use try-except blocks. A try block contains the code that may raise an error, while an except block contains the code that handles the error if it occurs.

Here's an example of how to handle a file not found error:

```python
try:
    with open('nonexistentfile.txt') as f:
        data = f.read()
except FileNotFoundError:
    print("File not found")
```

In this example, we try to open a file that does not exist. Since the file is not found, a FileNotFoundError is raised. The except block catches the error and prints a message.

Another common error when working with files is a read or write error. For example, a file may be opened in read mode, but an attempt is made to write to it. Here's an example of how to handle a read/write error:

```python
try:
    with open('myfile.txt', 'r') as f:
        f.write('Hello, World!')
except IOError:
    print("Error writing to file")
```

In this example, we try to write to a file that is opened in read mode, which raises an IOError. The except block catches the error and prints a message.

It's always a good practice to include error handling in your file handling code to prevent unexpected errors from crashing your program.