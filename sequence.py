import RPi.GPIO as GPIO
import time
import math
import random


pins = {'tree1': 11, 'tree2': 13, 'led': 15, 'led2': 29}
pinarray = pins.values() # values of pins array 

GPIO.setmode(GPIO.BOARD)

for pin in pins.values():
    GPIO.setup(pin, GPIO.OUT)

def blink(pin, delay):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(pin, GPIO.LOW)

def blink_list(pins, delay):
    for pin in pins:
        GPIO.output(pin, GPIO.HIGH)
    time.sleep(delay)
    for pin in pins:
        GPIO.output(pin, GPIO.LOW)

def pause(pin, delay):
    GPIO.output(pin, GPIO.LOW)
    time.sleep(delay)

def variable_delay(initial_time, time, pins, pause_len=0, limit=.05):  # pause_len default value is 0 if not passed, limit default = 0.5
    """ pins is a list of pin numbers"""
    blink_delay = (initial_time - limit)* math.e ** (-.1 * time) + limit # decay toward limit seconds
    print blink_delay
    for pin in pins:
        blink(pin, blink_delay)
        pause(pin, pause_len)
    return blink_delay
    

def constant_delay(iterations, initial_time, pins, pause_len=0):
    x = 0
    for i in range(iterations):
        x = variable_delay(initial_time, 0, pins, pause_len)
    return x

final_blink_delay = 0.1



for i in range(50):
    final_blink_delay = variable_delay(1, i, pins.values()) 

constant_delay(20, final_blink_delay, pins.values())
constant_delay(6, .2, [pins['tree2']], .1) 
constant_delay(8, final_blink_delay, pins.values()[0::2])   
for i in range(40):
    variable_delay(random.uniform(.02,.3), 0, [random.choice(pins.values())])
    
GPIO.cleanup()
