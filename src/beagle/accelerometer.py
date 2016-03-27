def acc():
	from Adafruit_I2C import Adafruit_I2C
	from time import sleep
	# initialize i2c connection to MPU6050
	# i2c address is 0x68
	i2c = Adafruit_I2C(0x68)
	# wake up the device (out of sleep mode)
	# bit 6 on register 0x6B set to 0
	i2c.write8(0x6B, 0)
	print("X axis accelerations (in g's)")
	# read and print acceleration on x, y, z axis
	# Combined to obtain raw acceleration data
	while(1):
		print("X axis accelerations (in g's)")
		#getting values from the registers
		b = i2c.readS8(0x3b)
		s = i2c.readU8(0x3c)
		# converting 2 8 bit words into a 16 bit
		# signed "raw" value
		raw = b * 256 + s
		# still needs to be converted into G-forces
		g = raw / 16384.
		print (str(g))
		# print x accelerations.
		print("Y axis accelerations (in g's)")
		b = i2c.readS8(0x3d)
		s = i2c.readU8(0x3e)
		raw = b * 256 + s
		g = raw / 16384.
		print (str(g))
		# print y accelerations.
		print("Z axis accelerations (in g's)")
		b = i2c.readS8(0x3f)
		s = i2c.readU8(0x40)
		raw = b * 256 + s
		g = raw / 16384.
		print (str(g))
		# print z accelerations.
		sleep(1)
