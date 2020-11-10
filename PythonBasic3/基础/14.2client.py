#14.2client.py
import socket
s = socket.socket()
host = socket.gethostname()
port = 2345
s.connect((host, port))
print(s.recv(1024))