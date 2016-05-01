from __future__ import print_function
import socket
import sys


class TCPclient:
    def __init__(self,host,port):
        self.host = host
        self.port = port

    def connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.sock.connect((self.host,self.port))
            print("Connected")
        except:
            print("Cannot Connect to host")

    def send(self,msg):
        if sys.version_info.major == 2:
            self.sock.sendall(msg + "\n")

            # Receive data from the server and shut down
            received = self.sock.recv(1024)
        else:
            # Connect to server and send data
            self.sock.sendall(bytes(msg + "\n", "utf-8"))

            # Receive data from the server and shut down
            received = str(self.sock.recv(1024), "utf-8")
        if received:
            print("Send successful")

    def stop(self):
        self.sock.close()

if __name__ == "__main__":
    HOST, PORT = 'localhost',9999

    client = TCPclient(HOST,PORT)

    client.connect()

    try:
        while 1:
            if sys.version_info.major == 2:
                data = raw_input("Input message:")
                client.send(data)

            else:
                data = input("Input Message:")
                client.send(data)
    except:
        print("Program stopped")
        client.stop()
