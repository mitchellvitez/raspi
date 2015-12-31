import RPi.GPIO as GPIO
import time, math, random, sys
from operator import itemgetter 

pins = [
        [15, 33, 91, 92],
        [13, 31, 93, 94],
        [11, 29, 95, 96],
        [81, 82, 83, 84],
        [85, 86, 87, 88]
        ]
"""
In Python, we index with array[row][column]

Rows at columns both have their origin at the top left,
and increase in the down and right directions

They start from 0

The following is a 4x5 matrix, dimensions are m by n, like in math

    col->
row  (0,0) (0,1) (0,2) (0, 3) (0, 4) 
 |   (1,0) (1,1) (1,2) (1, 3) (1, 4)
 V   (2,0) (2,1) (2,2) (2, 3) (2, 4)
     (3,0) (3,1) (3,2) (3, 3) (3, 4)

The number of rows is len(matrix)
and the number of columns is len(matrix[0]),
since matrix[0] is the first row in the matrix

Row 1 = pins[0]
Row 2 = pins[1]
Row 3 = pins[2]

Column 1 = map(itemgetter(0), pins)
Column 2 = map(itemgetter(1), pins)
Column 3 = map(itemgetter(2), pins)

"""



no_rows = len(pins)
no_cols = len(pins[0])
# print no_rows, no_cols

onoff = [[False] * (no_rows + 1) for i in range(no_cols+1)]


def display():
    for row_at in range(no_rows):
        for col_at in range(no_cols):
            string_value1 = str(pins[row_at][col_at]) + ' '
#            sys.stdout.write(string_value1 if pins[row_at][col_at] == pins[row_at][col_at]-0  else ' - ')
            sys.stdout.write(' * ' if onoff[col_at][row_at] else ' - ')
        sys.stdout.write('\n')
    sys.stdout.write('\n')


def setup():
    GPIO.setmode(GPIO.BOARD)
    for row_at in range(no_rows):
        for col_at in range(no_cols):
            GPIO.setup(pins[col_at][row_at], GPIO.OUT)

def set_rect(first_col, last_col, bottom_row, top_row, illuminate_block=True, set_others_to_opposite =True):
#    print first_col, last_col, bottom_row, top_row, val, run_set_all 
    if set_others_to_opposite:
        set_all(not(illuminate_block))
    for col_at in range(first_col, last_col+1):
        for row_at in range(bottom_row, top_row+1):
             onoff[col_at][row_at] = illuminate_block
    val = True
    run_set_all = True

def set_all(val=False):
    set_rect(0, no_cols, 0, no_rows, val, False)

def set_row(num, val=True, run_set_all=True):
    set_rect(0, no_cols, num, num, val, run_set_all)

def set_col(num, val=True, run_set_all=True):
    set_rect(num, num, 0, no_rows, val, run_set_all)

def chaser(by_col=False, start_black=True, switch_old_to_start=False):
    set_all(not(start_black))
    if by_col:
        iii_end = no_rows
        jjj_end = no_cols
    else:
        jjj_end = no_rows
        iii_end = no_cols
    for iii in range(iii_end):
        start = 0
        stop = jjj_end
        step = 1
        if int(iii/2) * 2 == iii:
            start = jjj_end
            stop = -1
            step = -1
        for jjj in range(start, stop, step):
            if by_col:
                set_rect(jjj, jjj, iii, iii, start_black, switch_old_to_start)
            else:
                set_rect(iii, iii, jjj, jjj, start_black, switch_old_to_start)            
            display()

"""
set_rect(1,3,1,2)
display()

set_rect(1,1,3,4)
set_rect(2,2,1,2,True,False)  
display()

set_rect(2,2,1,2,False)
display()

set_row(1, False)
display()

set_row(3, False, False)
display()
"""
#chaser(True, False, False)
chaser(True, True, True)       

set_rect(1,3,1,3,False)
display()

set_rect(1,2,1,3,False)
display()

set_rect(1,3,1,4,False)
set_rect(3,3,0,2,True,False)
set_rect(0,3,2,2,True,False)
set_rect(2,2,3,3,True,False)
set_rect(3,3,4,4,True,False)
display()

set_rect(0,0, 0,2)
set_rect(2,2, 0,2, True, False)
set_rect(0,2, 2,2, True, False)
set_rect(1,1, 3,4, True, False)
display()



GPIO.cleanup()
