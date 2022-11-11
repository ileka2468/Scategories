import datetime

from games_settings import create_categories, generate_start_letters, game_settings
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
    username = input("Enter a username: ")
    start_game = input("\nEnter 'y' to start: ")
    game(username)


def game(username):
    previous_game_file = open(f"{username}_answers.txt", "w")
    previous_game_file.close()
    round_info = retreive_round_info()

    for round in range(settings):
        category = round_info[round][1]
        letter = round_info[round][2].strip()
        print(f"Category: {category} and Letter: {letter}")
        start_time = datetime.datetime.now().replace(microsecond=0)
        userText, timedOut = timedInput("Enter answer: ", 10)
        if(timedOut):
            print("------Sorry, times up------")

        else:
            print(f"Previous answer: '{userText}'")
            end_time = datetime.datetime.now().replace(microsecond=0)
            duration = str(end_time - start_time)

            print(f"You took {duration[5:]} seconds to complete this question!")
            saveAnswer(username, round, userText, category, letter)

def saveAnswer(player, round, answer, category, letter):
    with open(f"{player}_answers.txt", "a") as f:
        f.write(f"{round}, {category}, {letter}, {answer}\n")

def retreive_round_info():
    with open("settings.txt", "r") as f:
        round_settings = []
        for line in f:
            round_settings.append(line.split(","))
        return round_settings


def main():
    game_start()


main()

