from __future__ import print_function
import sys
import threading
import socket
if sys.version_info.major == 2:
    import SocketServer as ss
else:
    import socketserver as ss

class ThreadedTCPServer(ss.ThreadingMixIn, ss.TCPServer):
    pass


class TCP:
    def __init__(self,host,port,handler_func = None):
        self.host = host
        self.port = port

        class ThreadedTCPRequestHandler(ss.BaseRequestHandler):
            def handle(self):
                while 1:
                    data = self.request.recv(1024)
                    if not data:
                        break
                    if handler_func:
                        handler_func("%s"%data)
                    self.request.sendall('Received')

        self.handler = ThreadedTCPRequestHandler

    def start(self):
        self.server = ThreadedTCPServer((self.host,self.port),self.handler)
        self.server_thread = threading.Thread(target = self.server.serve_forever)
        self.server_thread.deamon = True
        self.server_thread.start()

    def stop(self):
        self.server.shutdown()
        self.server.server_close()

if __name__ == "__main__":
    print("This is a sub-module for Cobwebiot")
    '''
    import Queue
    import time

    HOST, PORT = "localhost", 9999

    msg_buffer = Queue.Queue()
    def MyTCPHandler(data):
        msg_buffer.put(data)

    # Create the server, binding to localhost on port 9999
    tcp_server = TCP(HOST,PORT,MyTCPHandler)

    try:
        tcp_server.start()

        while 1:
            if not msg_buffer.empty():
                temp_data = msg_buffer.get()
                print(temp_data)
            else:
                time.sleep(0.2)

    except:
        print("Finished")
        tcp_server.stop()
    '''
