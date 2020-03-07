import sys
import socket                     ##imports##
import time

s = socket.socket()
host = input(str("Enter the server name to connect:"))
port = 8080
s.connect((host,port))
print("connected to the chat server")
while 1:
    server_message = s.recv(2048)
    server_message = server_message.decode()
    print("server:", server_message)
    message = input(str(">>"))
    message = message.encode()
    s.send(message)
    print("message has been sent...")