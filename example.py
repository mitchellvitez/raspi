# So we can use GPIO later on
import RPi.GPIO as GPIO
import time

"""
Run this code with the command:
sudo python example.py

Edit on the raspi with:
vim example.py
in the terminal

Press
[ctrl]+[c]
to stop script execution
"""

# Takes a pin number and a delay in seconds
# Makes that pin HIGH for delay seconds, then turns it to LOW
def blink(pin, delay):
	GPIO.output(pin, GPIO.HIGH)
	time.sleep(delay)
	GPIO.output(pin, GPIO.LOW)

# Sets pin 11 to HIGH for at least delay seconds
def on(pin, delay):
	GPIO.output(pin, GPIO.HIGH)
	time.sleep(delay)

def off(pin, delay):
	GPIO.output(pin, GPIO.LOW)
	time.sleep(delay)

def onUntilChanged(pin):
	GPIO.output(pin, GPIO.HIGH)

def offUntilChanged(pin):
	GPIO.output(pin, GPIO.HIGH)

# Necessary setup step
GPIO.setmode(GPIO.BOARD)
# Pin number 11 -> GPIO.OUT
GPIO.setup(11, GPIO.OUT)

# Waits for one second before continuing
time.sleep(1)

speed_factor = 0.5

# does this 10 times
for num in range(10):
	# on for speed_factor seconds
	on(speed_factor)
	# off an increasing amount (since num goes from 0 to 10)
	off(num * speed_factor)

onUntilChanged(11)

# Necessary cleanup step
GPIO.cleanup()

