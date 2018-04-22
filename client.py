import socket
import sys
import time

host = 'localhost'
port = 50000
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))

while 1:
    msg = input("\nSend to server:")
    s.send(msg.encode())

    data = s.recv(size)
    sys.stdout.write("msg from server:" + data.decode())
s.close()