import datetime

from GameSettings import create_categories, generate_start_letters, game_settings
from art import *
from pytimedinput import timedInput
import datetime

'''
This is a final project for CSC 241 at DePaul Univeersity, Professor: Tony Lowe, Group Members: William Ileka, Bakhodir Astanov, Fouzan Hussain, Syed Farhan
Project: Scategories
License: MIT 

Copyright 2022 William Ileka Et al.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


'''
# loads in data by calling the functions from module GameSettings file
categories = create_categories()
start_letters = generate_start_letters()
settings = game_settings()

# function that generates the allowed player numbers, for validation purposes when the game starts
def allowed_usernames(player_num):
    string = ""
    for num in range(1, player_num + 1):
        string += f"{num},"
    new = string.rstrip(string[-1])
    return new


def game_start():
    welcome_message = text2art("Welcome to Scattergories!")
    print(welcome_message)
    print(f"---- Instructions ----\nYou will be given a category and a letter. Your job is to correctly enter as many items"
          f" from that category STARTING with that letter in your alotted time. You will have 30 seconds for each question.")
    print(f"\nThis game has {settings[1]} player(s). Choose your player number below")
    username, timeout = timedInput("Enter player number: ", timeout=-1, allowCharacters=f"{allowed_usernames(settings[1])}")
    timedInput("\nEnter 'y' to start: ", timeout=-1, allowCharacters="y")
    game(username)


def game(username):
    previous_game_file = open(f"{username}_answers.txt", "w")
    previous_game_file.close()
    round_info = retreive_round_info()

    for round in range(settings[0]):
        category = round_info[round][1]
        letter = round_info[round][2].strip()
        print(f"----------- Round {round + 1} -----------")
        print(f"Category: {category} and Letter: {letter}")
        start_time = datetime.datetime.now().replace(microsecond=0)
        userText, timedOut = timedInput("Enter answer: ", 30)
        if(timedOut):
            print("------Sorry, times up------")
            saveAnswer(username, round, "OOT", category, letter)

        else:
            end_time = datetime.datetime.now().replace(microsecond=0)
            duration = str(end_time - start_time)

            print(f"You took {duration[5:]} seconds to complete this question!")
            saveAnswer(username, round, userText.capitalize(), category, letter)
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

