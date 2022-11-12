import datetime

from GameSettings import create_categories, generate_start_letters, game_settings
from art import *
from pytimedinput import timedInput
import datetime

categories = create_categories()
start_letters = generate_start_letters()
settings = game_settings()


def game_start():
    welcome_message = text2art("Welcome to Scattergories!")
    print(welcome_message)
    print(f"---- Instructions ----\nYou will be given a category and a letter. Your job is to correctly enter as many items"
          f" from that category STARTING with that letter in your alotted time. You will have 30 seconds for each question.")
    print(f"\nThis game has {settings[1]} player(s). Choose your player number below")
    username = input("Enter player number: ")
    timedInput("\nEnter 'y' to start: ", timeout=-1, allowCharacters="y")
    game(username)


def game(username):
    previous_game_file = open(f"{username}_answers.txt", "w")
    previous_game_file.close()
    round_info = retreive_round_info()

    for round in range(settings[0]):
        category = round_info[round][1]
        letter = round_info[round][2].strip()
        print(f"Category: {category} and Letter: {letter}")
        start_time = datetime.datetime.now().replace(microsecond=0)
        userText, timedOut = timedInput("Enter answer: ", 30)
        if(timedOut):
            print("------Sorry, times up------")
            saveAnswer(username, round, "OOT", category, letter)

        else:
            print(f"Previous answer: '{userText}'")
            end_time = datetime.datetime.now().replace(microsecond=0)
            duration = str(end_time - start_time)

            print(f"You took {duration[5:]} seconds to complete this question!")
            saveAnswer(username, round, userText, category, letter)
        if round == settings[0] - 1:
            print(f"The game has ended, your answers have been recorded in {username}_answers.txt. Send this file to the person who will be scoring it.")

def saveAnswer(player, round, answer, category, letter):
    with open(f"{player}_answers.txt", "a") as f:
        f.write(f"{round}, {category}, {letter}, {answer}\n")

def retreive_round_info():
    with open("settings.txt", "r") as f:
        round_settings = []
        next(f)
        for line in f:
            round_settings.append(line.split(","))
        return round_settings


def main():
    game_start()


main()

