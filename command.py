import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

import sys

while True:
	x = raw_input('Please enter a command (on/off/quit): ')
	if x == 'quit':
		GPIO.cleanup()
		sys.exit()
	elif x == 'on':
		GPIO.output(11, GPIO.HIGH)
	elif x == 'off':
		GPIO.output(11, GPIO.LOW)


