import RPi.GPIO as GPIO
import time

def blink(pin, delay):
	GPIO.output(pin, GPIO.HIGH)
	time.sleep(delay)
	GPIO.output(pin, GPIO.LOW)
	time.sleep(.05)

def on(delay):
	GPIO.output(11, GPIO.HIGH)
	time.sleep(delay)

def off(delay):
	GPIO.output(11, GPIO.LOW)
	time.sleep(delay)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

SPEED = .19

import random

for num in range(0, 500):
	on(1 * SPEED)
	off(2 * SPEED)
	on(1 * SPEED)
	off(2 * SPEED)
	on(2 * SPEED)
	off(2 * SPEED)

GPIO.cleanup()

