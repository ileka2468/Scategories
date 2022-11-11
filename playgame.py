import time
from games_settings import create_categories, generate_start_letters, game_settings
from art import *
import random
import msvcrt
import sys

categories = create_categories()
start_letters = generate_start_letters()
settings = game_settings()

class TimeoutExpired(Exception):
    pass

def input_with_timeout(prompt, timeout, timer=time.monotonic):
    sys.stdout.write(prompt)
    sys.stdout.flush()
    endtime = timer() + timeout
    result = []
    while timer() < endtime:
        if msvcrt.kbhit():
            result.append(msvcrt.getwche()) #XXX can it block on multibyte characters?
            if result[-1] == '\r':
                return ''.join(result[:-1])
        time.sleep(0.04) # just to yield to other processes/threads
    raise TimeoutExpired

def game_start():
    welcome_message = text2art("Welcome to Scattergories!")
    print(welcome_message)
    print(f"---- Instructions ----\nYou will be given a category and a letter. Your job is to correctly enter as many items"
          f" from that category STARTING with that letter in your alotted time. Time left is indicated by the progress bar.")
    start_game = input("\nEnter 'y' to start: ")
    game()


def game():
    for num in range(settings[0]):
        category = random.choice(list(categories.keys()))
        letter = random.choice(list(start_letters[category]))
        print(f"Category: {category} and Letter: {letter}")
        try:
            answer = input_with_timeout("Enter your answer: ", 10)
        except TimeoutExpired:
            print('\n ------Sorry, times up------')
        else:
            print('Got %r' % answer)



def main():
    game_start()

main()

