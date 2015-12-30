import RPi.GPIO as GPIO
import time
import random
import pygame
import math
import sys

def on(pin):
    GPIO.output(pin, GPIO.HIGH)

def off(pin):
    GPIO.output(pin, GPIO.LOW)

def on_delay(pin, delay):
    on(pin)
    time.sleep(delay)

def off_delay(pin, delay):
    off(pin)
    time.sleep(delay)

def countdown(pin):
    for i in range(3, 0, -1):
        print i
        on(pin)
        time.sleep(.5)
        off(pin)
        time.sleep(.5)

def selection():
    while True:
        for event in pygame.event.get():
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                return True
            if pygame.key.get_pressed()[ord('q')]:
                return False

def readable_time(reaction_time):
    x = int(math.ceil(reaction_time * 1000))
    if x > 1000:
        return str(x / 1000.0) + " seconds"
    return str(x) + " milliseconds"
    
def buzz(pin):
    for i in range(15):
        on(pin)
        time.sleep(.03)
        off(pin)
        time.sleep(.03)

def hello(pin):
    for i in range(20, 0, -1):
        on(pin)
        time.sleep(i * .005)
        off(pin)
        time.sleep(i * .005)
    for i in range(3):
        # 121222
        on_delay(pin, .1)
        off_delay(pin, .2)
        on_delay(pin, .1)
        off_delay(pin, .2)
        on_delay(pin, .2)
        off_delay(pin, .2)

def goodbye(pin):
    for i in range(20):
        on(pin)
        time.sleep(i * .005)
        off(pin)
        time.sleep(i * .005)

def success(pin, reaction_time):
    for i in range(4):
        on(pin)
        time.sleep(reaction_time / 7.0)
        off(pin)
        time.sleep(reaction_time / 7.0)
        on(pin)
        time.sleep(.21)
        off(pin)
        time.sleep(.21)

def delay(pin):
    delay = random.uniform(1, 10)
    start_of_delay = time.time()
    cheated = False
    while start_of_delay + delay > time.time() and not cheated:
        for event in pygame.event.get():
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                print "You cheated! Try again."
                buzz(pin)
                return True
    return False

def save_high_score(time, name):
    s = time + " " + name + "\n"
    with open("react-highscores.txt", "a") as f:
        f.write(s)
    with open("react-highscores.txt", "w+") as f:
        x = f.readlines()
        for line in sorted(x):
            f.write(line)

def setup(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    
    GPIO.setup(pin, GPIO.OUT)
    pygame.init()

    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("REACT!")

    print """Welcome to React!, a game that tests your reaction skills
Press the space bar to begin a game
Press the space bar again once the light turns on
Enjoy!
"""

def run_game(pin, name):
    on(pin)
    print "GO!"
    time_turned_on = time.time()
    
    active = True
    old_press = False
    while active:
        for event in pygame.event.get():
            if pygame.key.get_pressed()[pygame.K_SPACE] and not old_press:
                active = False
            old_press = pygame.key.get_pressed()[pygame.K_SPACE]

    reaction_time = time.time() - time_turned_on
    print "Your reaction time was", readable_time(reaction_time)
    success(pin, reaction_time)
    # TODO: implement high scores
    # save_high_score(readable_time(reaction_time), name)

def main():
    PIN = 11
    setup(PIN)

    hello(PIN)
    # TODO: use this for high scores
    # name = raw_input("Enter the name you'd like to use for high scores: ")
    name = ""
    
    game_is_running = True
    while game_is_running:
        off(PIN)
        
        print "\nPress space to begin a new round or q to quit"
        game_is_running = selection()
        if not game_is_running:
            break
        
        countdown(PIN)
        cheated = delay(PIN)
                    
        if not cheated:
            run_game(PIN, name)

    goodbye(PIN)
    GPIO.cleanup()

if __name__ == "__main__":
    main()
