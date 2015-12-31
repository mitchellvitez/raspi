import RPi.GPIO as GPIO
import time, math, random, sys
from operator import itemgetter

from mv_array import *

def main():
    setup()
    run()
    GPIO.cleanup()

def run():
    MODE = CARTESIAN
    
    rectangle(first_col = 0, last_col = 0, first_row = 1, last_row = 3, value = True)
    point(col = 1, row = 2, value = True)
    display()
    
    all(True)
    display()
    
    all(False)
    display()

    col(1)
    row(2)
    display()

    all(False)
    col(2)
    row(2)
    display()

    MODE = DEFAULT

    all(True)
    display()
   
if __name__ == '__main__':
    main()
    
