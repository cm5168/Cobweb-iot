from __future__ import print_function
import cobwebiot.beagle.adc as Badc
from time import sleep

adc = Badc.ADC()

adc.start()

print("Acceleration")
while(1):
	g = adc.read()
	print("Voltage : %.4f"%g)
	sleep(1)