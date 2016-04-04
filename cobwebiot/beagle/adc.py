import Adafruit_BBIO.ADC as BADC

class ADC:
	def __init__(self):
		self.g=0
		self.sensor_pin = 'P9_40'
		self.ADC = BADC
	def start(self):
		self.ADC.setup()
	def read(self):
		self.g = self.ADC.read(self.sensor_pin)
		return self.g*1.800