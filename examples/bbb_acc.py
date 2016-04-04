from __future__ import print_function
import cobwebiot.beagle.acc as Bacc
from time import sleep

acc = Bacc.ACC()

acc.start()

print("Acceleration")
while(1):
	g = acc.read()
	print("   x   |   y   |   z   ")
	print("%7.5f|%7.5f|%7.5f"%(g[0],g[1],g[2]))
	sleep(1)