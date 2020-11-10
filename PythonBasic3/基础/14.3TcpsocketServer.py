#14.3创建多线程类型的TCP SocketServer
import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
　　 客户端发送a-z字符串，socketserver返回大写
    """

    def handle(self):    #必须要有handle方法；所有处理必须通过handle方法实现
        # self.request is the TCP socket connected to the client
        while True:
            self.data = self.request.recv(1024).strip()
            if not self.data:
                print('The client disconnects actively!')
                break
            self.return_client()

    def return_client(self):    #数据处理方法
        print("Ip:{0} Port{1}:".format(self.client_address[0], self.client_address[1]))
        print(self.data.decode('utf8'))
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())


if __name__ == "__main__":
    HOST, PORT = "127.0.0.1", 9990

    # Create the server, binding to localhost on port 9999
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)    #实例化一个多线程TCPServer
    print('Wait client . . .') 
    server.serve_forever()
