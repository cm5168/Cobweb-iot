from __future__ import print_function
import cobwebiot.beagle as bbb
from time import sleep


pin = "P8_10"
time = 1
bbb.blink(pin,time)
