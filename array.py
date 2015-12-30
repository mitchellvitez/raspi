import RPi.GPIO as GPIO
import time
import math
import random
import sys


pins = [[11, 13], [15, 29]]
onoff = [[False] * 4 for i in range(4)]


def setup():
    GPIO.setmode(GPIO.BOARD)
    for x in range(len(pins)):
        for y in range(len(pins)):
            GPIO.setup(pins[x][y], GPIO.OUT)

def display():
    for x in range(len(onoff)):
        for y in range(len(onoff)):
            sys.stdout.write('*' if onoff[x][y] else '-')
            sys.stdout.write('')
        sys.stdout.write('\n')
    sys.stdout.write('\n')

def rect(left, right, top, bottom, val=True):
    for x in range(left, right):
        for y in range(top, bottom):
            onoff[y][x] = val

def set_all(val=False):
    rect(0, 4, 0, 4, val)

def rowset(num, val=True):
    rect(0, 4, num, num + 1, val)

def columnset(num, val=True):
    rect(num, num + 1, 0, 4, val)

for row in range(2):
    for col in range(4):
        set_all()
        rect(col, col+1, row, row+1)
        display()

set_all()
rect(1,3,1,3)
display()

set_all(True)
rect(1,4,1,3,False)
display()

set_all(True)
rect(1,3,1,3,False)
display()

set_all(True)
rect(1,4,1,4,False)
display()

set_all(False)
rect(0,1, 0,2)
rect(2,3, 0,2)
rect(1,2, 1,2)
rect(1,2, 2,4)

display()

set_all()
for row in range(4):
    start = 0
    stop = 4
    step = 1
    if int(row/2) * 2 == row:
        start = 3
        stop = -1
        step = -1
    for col in range(start, stop, step):
#        set_all()
        rect(col, col+1, row, row+1)
        display()

set_all()
rowset(1)
display()

GPIO.cleanup()
