#14.4TCPsocketClient.py
import socket


HOST, PORT = "127.0.0.1", 9990

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

while True:
    data = input('Input [a-z]:>>')
    if data == 'bye': break
    sock.sendall(bytes(data + "\n", "utf-8"))
    received = str(sock.recv(1024), "utf-8")
    print("Sent:     {}".format(data))
    print("Received: {}".format(received))
sock.close()
