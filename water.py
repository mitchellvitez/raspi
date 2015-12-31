import RPi.GPIO as GPIO
import time, math, random, sys
from operator import itemgetter 
from collections import OrderedDict

outs = {'aaa': 15, 'bbb': 29}  #this is a dictionary with keys and values
outs = OrderedDict(sorted(outs.items(), key=lambda t: t[1]))

ins = {'xxx': 37, 'yyy': 33}
ins = OrderedDict(sorted(ins.items(), key=lambda t: t[1]))


def polling_delay(val=1):
    time.sleep(val)
    return val

def setup():
    GPIO.setmode(GPIO.BOARD)
    for i in range(len(outs)):
        GPIO.setup(outs.values()[i], GPIO.OUT)  #when referencing a dictionary, use .values
    for i in range(len(ins)):
        GPIO.setup(ins.values()[i], GPIO.IN)

setup()

sprinkler_on = False
while not sprinkler_on:
    polling_delay(1)
    print sprinkler_on
    sprinkler_on = GPIO.input(ins['xxx'])


print '  '
print ' Sprinkler is on? ', sprinkler_on
time.sleep(4)
    

pump_off_timer = 0
switching_delay = 5

for pin in outs.values():
    GPIO.output(pin, GPIO.LOW)
    time.sleep(2)


GPIO.output(outs['aaa'], GPIO.LOW)
#time.sleep(2)
    
GPIO.output(outs['aaa'], GPIO.HIGH)
GPIO.output(outs['bbb'], GPIO.HIGH)

while sprinkler_on:
    delay = polling_delay(.8)
    pump_off_timer = pump_off_timer + delay
    print pump_off_timer
    if pump_off_timer > switching_delay:
        print 'timed out'
        GPIO.output(outs['bbb'], GPIO.LOW)
    sprinkler_on = GPIO.input(ins['xxx'])
    

GPIO.cleanup()
