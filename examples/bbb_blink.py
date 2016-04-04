from __future__ import print_function
import cobwebiot.beagle.basic as Bbasic
from time import sleep


pin = "P8_10"
time = 1
Bbasic.blink(pin,time)
	