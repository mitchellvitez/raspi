import RPi.GPIO as GPIO
import time, math, random, sys
from collections import OrderedDict


pins = {'tree1': 11, 'tree2': 13, 'xled': 15, 'led2': 29}
pins = OrderedDict(sorted(pins.items(), key=lambda t: t[1]))

GPIO.setmode(GPIO.BOARD)

for pin in pins.values():
    GPIO.setup(pin, GPIO.OUT)
    print pin

def blink(pins, duration=.1, repeats=1, pause=0, val=True):
    for i in range(repeats):
        for pin in pins:
            GPIO.output(pin, GPIO.HIGH if val else GPIO.LOW)
            print pin, duration
            time.sleep(duration)
        for pin in pins:
            time.sleep(duration)
            GPIO.output(pin, GPIO.LOW if val else GPIO.HIGH)
            time.sleep(pause)

def e_decay_duration(initial_duration=0.5, count=1, decay_rate=.1, limit=.05):
    """ pins is a list of pin numbers"""
    duration = (initial_duration - limit)* math.e ** (-1 * decay_rate * count) + limit # decay toward limit seconds
    return duration
    
for i in range(4):
    duration = e_decay_duration(0.2, i)
    blink(pins.values(), duration)

blink(pins.values()[0:2], duration, 3)
blink([pins['tree2']], .2, 12, .3)
for i in range(3):
    blink([random.choice(pins.values())], random.uniform(0.02,.3))
    
GPIO.cleanup()
