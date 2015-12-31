import RPi.GPIO as GPIO
import time
import math
import random
import sys
import numpy

pins = [
        [15, 33],
        [13, 31],
        [11, 29]
    ]

# col1 = pins[0]
# col2 = pins[1]
def getColumnNumber(x):
    return pins[x - 1]


no_rows = len(pins)
no_cols = len(pins[0])
print no_cols, no_rows

onoff = [[False] * no_rows for i in range(no_cols)]

def display():
    for row_at in range(no_rows-1, -1, -1):
        for col_at in range(no_cols):
            sys.stdout.write('*' if pins[row_at][col_at] == 31  else '-')
        sys.stdout.write('\n')
    sys.stdout.write('\n')

display()


def setup():
    GPIO.setmode(GPIO.BOARD)
    for row_at in range(no_rows):
        for col_at in range(no_cols):
            GPIO.setup(pins[col_at][row_at], GPIO.OUT)
"""
def set_rect(1st_col, last_col, bottom_row, top_row, val=True, run_set_all = True):
    set_all() if run_set_all
    for col_at in range(1st_col, last_col+1):
        for y in range(bottom_row, top_row+1):
            onoff[col_at][row_at] = val

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

"""

GPIO.cleanup()
