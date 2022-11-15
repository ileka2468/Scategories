from pathlib import Path
from GameSettings import *
from pytimedinput import timedInput
global category_dict
from collections import defaultdict
category_dict = create_categories()

'''
This is a final project for CSC 241 at DePaul Univeersity, Professor: Tony Lowe, Group Members: William Ileka, Bakhodir Astanov, placeholder, placeholder
Project: Scategories
License: MIT 

Copyright 2022 William Ileka Et al.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


'''

def check_files(filenames, expected_files):
    for filename in filenames:
        path = Path(filename)
        if path.is_file():
            pass
        elif not path.is_file():
            raise Exception(f"I expected {filename} for player {filename[0]}, but did not see it in the directory!")


def get_files():
    with open("settings.txt", "r") as f:
        expected_players = int(f.readline()[18:])
        filenames = []
    for player_file in range(1, expected_players + 1):
        filenames.append(f"{player_file}_answers.txt")
    return (filenames, expected_players)


def generateanswersdict(player):
    answers = {}
    with open(f"{player}_answers.txt") as f:
        for line in f:
            split_line = line.split(",")
            temp_list = []
            for data in split_line:
                temp_list.append(data.strip())
            current_round = int(split_line[0])
            answers[current_round] = temp_list
        return answers


def genrateplayerdict(expected_players):
    player_dict = {}
    for player in range(1, expected_players + 1):
        player_dict[player] = generateanswersdict(player)
    return player_dict


def scoreGame(player_dict, player_num):
    # score players in sequential order
    scores_list = [0 for x in range(player_num)]
    for player in range(1, player_num + 1):
        score = 0
        for round in range(game_settings()[0]):
            answer = player_dict[player][round][3]
            answer_letter1 = player_dict[player][round][3][0]
            category = player_dict[player][round][1]
            letter = player_dict[player][round][2]
            if answer_letter1 == letter:
                if answer in category_dict[f"{category}"]:
                    scores_list[player - 1] += 1
    return scores_list


def reviewAnsers(player_dict, player_num, scores):
    compare_dict = {}
    with open("finalscore.txt", "w") as f:
        pass
    with open("Results.txt", "w") as f:
        pass
    for player in range(1, player_num + 1):
        score = 0
        print(f"---------- Player: {player} ----------")
        for round in range(game_settings()[0]):
            roundpoints = 0
            answer = player_dict[player][round][3]
            answer_letter1 = player_dict[player][round][3][0]
            category = player_dict[player][round][1]
            letter = player_dict[player][round][2]
            final_score(player, round, answer, category)
            if answer_letter1 == letter:
                if answer in category_dict[f"{category}"]:
                    roundpoints = 1
            formatting = f"Round: {round + 1}\nCategory: {category}\nLetter: {letter}\nAnswer: {answer}\nInitial Points Earned: {roundpoints}\n\n"
            print(formatting)
            writeResultsFile(formatting, player)

def writeResultsFile(string, player):
    with open("Results.txt", "a") as f:
        f.write(f"---------- Player: {player} ----------\n\n")
        f.write(string)




def final_score(player, round, answer,category):
    with open("finalscore.txt", "a") as f:
        f.write(f"{player},{round},{answer},{category}\n")


def score_finale(scorelist):
    for round in range(0, game_settings()[0]):
        with open("finalscore.txt", "r") as f2:
            # print(round)
            round_answers = []
            for line in f2:
                # print(line.split(",")[1], round)
                if line.split(",")[-2] in category_dict[str(line.split(",")[-1].strip())]:
                    if int(line.split(",")[1]) == round:
                        round_answers.append(line.split(",")[-2].strip())
                        # print(round_answers)
            find_dupes(round_answers, scorelist)


def find_dupes(round_list, scores_list):
    dupes = defaultdict(list)
    for index, answer in enumerate(round_list):
        dupes[answer].append(index)
    dupes = {k: v for k, v in dupes.items() if len(v) > 1}
    if len(dupes) > 0:
        # print("Same Answer Detected", dupes)
        for value in dupes.values():
            # print("----------newline----------")
            for num in value:
                print(f"Player {num + 1} lost points for having the same points as another player.")
                scores_list[num] -= 1
    global final_scoresforsure
    final_scoresforsure = scores_list


def writeFinalScore():
    with open("Results.txt", "a") as f:
        f.write(f"----------Final Score----------\n")
        for player in range(1, game_settings()[1] + 1):
            f.write(f"\nPlayer {player}: {final_scoresforsure[player - 1]}")


def main():
    files = get_files()
    check_files(files[0], files[1])
    player_dictionary = genrateplayerdict(files[1])
    score_list = scoreGame(player_dictionary, files[1])
    compare_dict = reviewAnsers(player_dictionary, files[1], score_list)
    score_finale(score_list)
    print(f"----------Final Score----------")
    for player in range(1, game_settings()[1] + 1):
        print(f"\nPlayer {player}: {final_scoresforsure[player - 1]}")
    writeFinalScore()

main()