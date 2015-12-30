import RPi.GPIO as GPIO
import time


def blink(pin, delay):
	GPIO.output(pin, GPIO.HIGH)
	time.sleep(delay)
	GPIO.output(pin, GPIO.LOW)
	time.sleep(.3)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

delay = .5

import random

for num in range(0, 500):
	blink(11, delay)
	delay = random.random() * 3

GPIO.cleanup()

