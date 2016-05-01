from Adafruit_I2C import Adafruit_I2C
import Adafruit_BBIO.ADC as BADC
import Adafruit_BBIO.GPIO as GPIO
import time

class ACC:
    def __init__(self):
        self.g=[0,0,0]
    def start(self):
        # initialize i2c connection to MPU6050
        # i2c address is 0x68
        self.i2c = Adafruit_I2C(0x68)
        # wake up the device (out of sleep mode)
        # bit 6 on register 0x6B set to 0
        self.i2c.write8(0x6B, 0)

    def read(self):
        # read and print acceleration on x, y, z axis
        # Combined to obtain raw acceleration data
        #print("X axis accelerations (in g's)")
        #getting values from the registers
        b = self.i2c.readS8(0x3b)
        s = self.i2c.readU8(0x3c)
        # converting 2 8 bit words into a 16 bit
        # signed "raw" value
        raw = b * 256 + s
        # still needs to be converted into G-forces
        self.g[0] = raw / 16384.
        #print (str(g[0]))
        # print x accelerations.
        #print("Y axis accelerations (in g's)")
        b = self.i2c.readS8(0x3d)
        s = self.i2c.readU8(0x3e)
        raw = b * 256 + s
        self.g[1] = raw / 16384.
        #print (str(g[1]))
        # print y accelerations.
        #print("Z axis accelerations (in g's)")
        b = self.i2c.readS8(0x3f)
        s = self.i2c.readU8(0x40)
        raw = b * 256 + s
        self.g[2] = raw / 16384.
        #print (str(g[2]))
        # print z accelerations.
        return g



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



def blink(pin,interval = 1):
    GPIO.setup(pin, GPIO.OUT)
    while True:
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(interval/2)
        GPIO.output(pin, GPIO.LOW)
        time.sleep(interval/2)
