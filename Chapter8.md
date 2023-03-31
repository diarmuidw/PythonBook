# Chapter 8: Networking with Python

# Introduction to Networking

Networking in computer science is the exchange of data between two or more devices. Networking enables devices, such as computers, smartphones, or IoT devices, to communicate with each other and share resources. Python provides several modules to develop networked applications. These modules can be used to develop client-server applications, chat applications, or web applications.

One of the simplest network programming examples is the `ping` command. This command sends an ICMP (Internet Control Message Protocol) "echo-request" message to a host, and waits for the host's reply. Here is an example of using the `ping` command to check if a host is reachable:

```python
import os

response = os.system("ping -c 1 google.com")

if response == 0:
    print("Ping successful!")
else:
    print("Ping failed!")
```

Python has several built-in modules for network programming, including `socket`, `asyncio`, `ssl`, `urllib`, `httplib`, and `ftplib`. These modules can be used to implement network protocols like HTTP, FTP, SMTP, Telnet, and SSH.

In this chapter, we will explore the `socket` module in more detail, which provides low-level network communication facilities. We will learn how to use the `socket` module to develop client-server applications, and also explore the `http.server` and `ftplib` modules to work with HTTP and FTP protocols.

# Sockets Programming

Sockets are the fundamental building blocks of network communication in Python. They are the endpoints of a two-way communication link that occurs between a client and a server. In Python, sockets are provided by the `socket` module, which allows you to create, bind, listen, and communicate with sockets.

The `socket()` function in the `socket` module creates a socket object that supports the specified address family (ipv4 or ipv6), socket type (stream or datagram), and protocol (default is 0). Here is an example of how to create a socket object:

```python
import socket

# create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

In the above example, we created a socket object using the `socket.socket()` function. We passed in two parameters to the function: the address family (`socket.AF_INET` for ipv4) and the socket type (`socket.SOCK_STREAM` for a TCP socket). 

Once you have a socket object, you can use it to connect to a server, send data to the server, and receive data from the server. Here is an example of how to connect to a server:

```python
import socket

# create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
server_address = ('localhost', 8000)
sock.connect(server_address)
```

In the above example, we connected to a server running on the local machine at port 8000. We used the `sock.connect()` method to establish the connection.

After you have established a connection, you can send data to the server using the `sock.send()` method and receive data from the server using the `sock.recv()` method. Here is an example of how to send and receive data:

```python
import socket

# create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
server_address = ('localhost', 8000)
sock.connect(server_address)

# send data to the server
message = 'Hello, server!'
sock.send(message.encode())

# receive data from the server
data = sock.recv(1024)

# print the received data
print(data.decode())
```

In the above example, we sent the message "Hello, server!" to the server using the `sock.send()` method. We then received data from the server using the `sock.recv()` method and printed it to the console.

Sockets can also be used to create server applications that listen for incoming connections. Here is an example of how to create a simple echo server:

```python
import socket

# create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to a specific address and port
server_address = ('localhost', 8000)
sock.bind(server_address)

# listen for incoming connections
sock.listen(1)

while True:
    # wait for a connection
    connection, client_address = sock.accept()
    
    try:
        # receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(1024)
            if data:
                connection.sendall(data)
            else:
                break
    finally:
        # close the connection
        connection.close()
```

In the above example, we created a socket object and bound it to the address `localhost` and port `8000`. We then listened for incoming connections using the `sock.listen()` method. Once a connection is established, we receive data from the client using the `connection.recv()` method and send it back to the client using the `connection.sendall()` method.

Sockets programming is a powerful tool for building networked applications in Python. It allows you to create both client and server applications that can communicate with each other over the network.

## Setting up Clients and Servers

In networking, clients and servers are two different programs that interact with each other to exchange data. The server is a program that listens to a specific port and responds to client requests. A client, on the other hand, is a program that sends requests to the server. 

Python provides several libraries to set up clients and servers. The `socket` module is one of the most commonly used libraries for communication over the network. 

To create a server, we first need to create a socket object using the `socket()` function with the appropriate parameters. We then bind the socket to a specific IP address and port number using the `bind()` method. Finally, we listen to incoming requests using the `listen()` method and accept incoming connections using the `accept()` method.

```python
import socket

# Create socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific IP address and port number
server_socket.bind(('localhost', 8080))

# Listen to incoming requests
server_socket.listen(1)

# Accept incoming connections
client_socket, address = server_socket.accept()

print('Connected by', address)

# Receive data from the client
data = client_socket.recv(1024)

# Send a response back to the client
client_socket.sendall(b'Received: ' + data)

# Close the connection
client_socket.close()
```

To create a client, we need to create a socket object and connect it to the server's IP address and port number using the `connect()` method. We can then send data to the server using the `sendall()` method and receive data from the server using the `recv()` method.

```python
import socket

# Create socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(('localhost', 8080))

# Send data to the server
client_socket.sendall(b'Hello, server!')

# Receive data from the server
data = client_socket.recv(1024)

print(repr(data))

# Close the connection
client_socket.close()
```

In the code examples above, we create a server that listens on port 8080 and a client that connects to this server. Once the client sends data to the server, the server responds with the same data preceded by the text `Received:`. 

This is a very basic example of networking with Python, but it demonstrates how we can set up a simple client-server architecture.

# Working with HTTP and FTP

Python provides in-built modules for working with HTTP and FTP protocols. These modules help in making HTTP/FTP requests, handling responses, and managing files over the protocol.

## HTTP

Python provides the `http.client` module to work with the HTTP protocol. Using this module, we can make HTTP requests to a server and handle the response. Let's look at an example:

```python
import http.client

# Create a connection to the server
conn = http.client.HTTPSConnection("www.google.com")

# Send a GET request
conn.request("GET", "/")

# Get the response from the server
res = conn.getresponse()

# Print the response status code
print(res.status)

# Print the response body
print(res.read())
```

In the above example, we create an HTTPS connection to the Google server and send a GET request to the root directory of the website. We then get the response from the server and print the status code and the response body.

## FTP

Python provides the `ftplib` module to work with the FTP protocol. Using this module, we can connect to an FTP server, navigate through directories, and upload/download files. Let's look at an example:

```python
import ftplib

# Create a connection to the FTP server
ftp = ftplib.FTP("ftp.example.com")

# Login to the server
ftp.login("username", "password")

# Navigate to a directory
ftp.cwd("/public_html")

# Upload a file to the server
with open("example.txt", "rb") as f:
    ftp.storbinary("STOR example.txt", f)

# Download a file from the server
with open("example.txt", "wb") as f:
    ftp.retrbinary("RETR example.txt", f.write)

# Logout from the server
ftp.quit()
```

In the above example, we create a connection to an FTP server, login using the username and password, navigate to a directory, upload a file to the server, download a file from the server, and finally, logout from the server. 

## Conclusion

Python provides easy-to-use modules for working with HTTP and FTP protocols. These modules simplify the process of making requests, handling responses, and managing files over the protocols.