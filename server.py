import sys
import socket                     ##imports##
import time

s = socket.socket()
host = socket.gethostname()
print('server will be running on host:',host)      #tells the host name#
port = 8080
s.bind((host,port))
print("binding done succesfully")
print("server is waiting for the incomming connecetions")
s.listen(1)
conn,addr = s.accept()
print(addr,"has connected to the server and now is online")

while 1 :
    message = input(str(">>"))
    message = message.encode()
    conn.send(message)
    print("message has been sent...")
    server_message = conn.recv(2048)
    server_message = server_message.decode()
    print("server:", server_message)