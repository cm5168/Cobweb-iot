from __future__ import print_function
from cobwebiot import client
import sys


HOST, PORT = '155.246.203.44',9999

cc = client.TCPclient(HOST,PORT)

cc.connect()

try:
    while 1:
        if sys.version_info.major == 2:
            data = raw_input("Input message:")
            cc.send(data)

        else:
            data = input("Input Message:")
            cc.send(data)
except:
    print("Program stopped")
    cc.stop()
