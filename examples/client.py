from cobwebiot import client
import sys

while 1:
	if sys.version_info.major == 2:
		a = raw_input("Enter Message:")
	else:
		a = input("Enter Message:")
	client.send('localhost',9999,a)
