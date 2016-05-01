from __future__ import print_function
from cobwebiot import client
import sys


HOST, PORT = 'localhost',9999

client = client.TCPclient(HOST,PORT)

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
