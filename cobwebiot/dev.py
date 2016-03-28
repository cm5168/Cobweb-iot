class mcp3008():
	def __init__(self):
	
	def get_xfer2(self,channel):
		return [1,(8+channel)<<4,0]
		
	def hex_to_data(self, upper, lower):
		return ((upper&3) << 8) + lower

		
class tmp36():
	def __init__(self):
	
	def get_temp(self, raw_data, voltage, round_places = 4):
		return round((data*330)/float(1023)-50,places)
	
	
class ldr():
	def __init__(self):
	
	def get_level(self, raw_data, voltage, round_places = 4):
		return round((data*3.3)/float(1023),places)