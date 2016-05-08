from __future__ import print_function
from cobwebiot import server
import Queue
import time

HOST, PORT = "localhost", 9999

msg_buffer = Queue.Queue()
def MyTCPHandler(data):
    msg_buffer.put(data)

tcp_server = server.TCP(HOST,PORT,MyTCPHandler)

try:
    tcp_server.start()
    f = open('text.txt','w')
    while 1:
        if not msg_buffer.empty():
            temp_data = msg_buffer.get()
            f.write(temp_data)
            print(temp_data)
        else:
            time.sleep(0.2)
    f.close()
except:
    print("Finished")
    tcp_server.stop()
