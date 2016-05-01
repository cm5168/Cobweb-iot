import socket
import threading
import os

def sendfile(name, sock):
    filename = sock.recv(1024)
    if os.path.isfile(filename):
        sock.send("EXISTS " + str(os.path.getsize(filename)))
        userResponse = sock.recv(1024)
        if userResponse[:2] == 'OK':
            with open(filename, 'rb') as f:
                bytesToSend = f.read(1024)
                sock.send(bytesToSend)
                while bytesToSend != "":
                    bytesToSend = f.read(1024)
                    sock.send(bytesToSend)
    else:
        sock.send("DO Not HAVE this file ")

    sock.close()

def Main():
    host = socket.gethostname()
    port = 9999
    s = socket.socket()
    s.bind((host,port))
    s.listen(5)
    print "Server Started."
    while 1:
        c, addr = s.accept()
        print "client connedted ip:<" + str(addr) + ">"
        t = threading.Thread(target=sendfile, args=("RetrThread", c))
        t.start()
    s.close()

if __name__ == '__main__':
    Main()
