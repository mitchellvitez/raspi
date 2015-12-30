import RPi.GPIO as GPIO
import time

def blink(pin, delay):
	GPIO.output(pin, GPIO.HIGH)
	time.sleep(delay)
	GPIO.output(pin, GPIO.LOW)
	time.sleep(delay)
	return

def sos(pin):
	for i in range(3):
		blink(pin, .08)
	time.sleep(.4)
	for i in range(3):
		blink(pin, .5)
	for i in range(3):
		blink(pin, .08)
	GPIO.output(pin, GPIO.LOW)
	time.sleep(1)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

for i in range(50):
	sos(11)

GPIO.cleanup()
