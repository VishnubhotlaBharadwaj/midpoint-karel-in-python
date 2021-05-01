from karel.stanfordkarel import *

def turn_around():
    turn_left()
    turn_left()
def main():
    put_beeper()
    if front_is_clear():
        move()
        if front_is_clear():
            findMid()
            remove_all_beepers()
            middle()
        else:
            turn_around()
            middle()

def findMid():
    placebeeperwall()
    while no_beepers_present():
        is_it_mid()
        find_beeper()

def remove_all_beepers():
    pick_beeper_alg()
    turn_around()
    middle()
    pick_beeper_alg()
    turn_around()

def pick_beeper_alg():
    while front_is_clear():
        move()
        pick_beeper()

def middle():
    while no_beepers_present():
        move()

def placebeeperwall():
    while front_is_clear():
        move()
    put_beeper()
    turn_and_move()

def is_it_mid():
    move()
    if beepers_present():
        turn_and_move()
        put_beeper()

def find_beeper():
    if no_beepers_present():
        while no_beepers_present():
            move()
        turn_and_move()
        put_beeper()
        move()

def turn_and_move():
    turn_around()
    move()

if __name__ == ' __main__':
    run_karel_program('Midpoint.w')

