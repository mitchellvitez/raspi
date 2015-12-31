import RPi.GPIO as GPIO
import time, math, random, sys
from operator import itemgetter

DEFAULT = 0
CARTESIAN = 1

# Important! Change the following value to get the indexing style you prefer
MODE = CARTESIAN

PINS = [
        [15, 33],
        [13, 31],
        [11, 29],
    ]

NUM_ROWS = len(PINS)
NUM_COLS = len(PINS[0])

GRID = [[False] * NUM_COLS for i in range(NUM_ROWS)]

def main():
    setup()
    test()
    GPIO.cleanup()

def test():
    # See mv_lightshow.py for actual code that builds on this library
    all(True)
    display()
    
def display():
    """Prints out the grid to the terminal, using * for a light"""
    global GRID
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS):
            sys.stdout.write('*' if GRID[row][col] else '-')
        print
    print
    # TODO: Write code that translates this into the output GPIO pin HIGH/LOW signals

def setup():
    """Connects to GPIO pins and prepares for output"""
    GPIO.setmode(GPIO.BOARD)
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS):
            GPIO.setup(PINS[row][col], GPIO.OUT)

def point(row, col, value=True):
    global GRID
    
    if MODE == DEFAULT:
        GRID[row][col] = value
    elif MODE == CARTESIAN:
        GRID[NUM_ROWS - row][col - 1] = value

def rectangle(first_row, last_row, first_col, last_col, value=True):
    if last_row < first_row:
        last_row, first_row = first_row, last_row
    if last_col < first_col:
        last_col, first_col = first_col, last_col

    for row in range(first_row, last_row + 1):
        for col in range(first_col, last_col + 1):
            point(row, col, value)

def rectangle_range(rows, cols, value=True):
    rectangle(rows[0], rows[-1], cols[0], cols[-1], value)
            
def all(value=True):
    global GRID
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS):
            GRID[row][col] = value

def row(num, value = True):
    for col in (range(NUM_COLS) if MODE == DEFAULT else range(1, NUM_COLS + 1)):
        point(num, col, value)
        
def col(num, value = True):
    for row in (range(NUM_ROWS) if MODE == DEFAULT else range(1, NUM_ROWS + 1)):
        point(row, num, value)

if __name__ == '__main__':
    main()
    
