#14.1server
import socket
s = socket.socket()
host = socket.gethostname()
port = 2345
s.bind((host, port))#1.绑定
s.listen(5)#2.监听
while True:
    c, addr = s.accept()#3.接收
    print('Got connection from', addr)
    str='Thank you for connecting'.encode('utf8')
    c.send(str)
    
    c.close()