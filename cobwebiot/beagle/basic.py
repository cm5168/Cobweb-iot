import Adafruit_BBIO.GPIO as GPIO

def blink(pin,time = 1):
	GPIO.setup(pin, GPIO.OUT)
	while True:
		GPIO.output(pin, GPIO.HIGH)
		time.sleep(time/2)
		GPIO.output(pin, GPIO.LOW)
		time.sleep(time/2)
		