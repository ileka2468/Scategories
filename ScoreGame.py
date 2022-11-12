from pathlib import Path
from GameSettings import *
from pytimedinput import timedInput
global category_dict
category_dict = create_categories()



def check_files(filenames, expected_files):
    for filename in filenames:
        path = Path(filename)
        if path.is_file():
            pass
        elif not path.is_file():
            raise Exception(f"I expected {filename}, but did not see it in the directory!")


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
    for player in range(1, 3):
        score = 0
        for round in range(game_settings()[0]):
            answer = player_dict[player][round][3]
            answer_letter1 = player_dict[player][round][3][0]
            category = player_dict[player][round][1]
            letter = player_dict[player][round][2]
            if answer_letter1 == letter:
                if answer in category_dict[f"{category}"]:
                    scores_list[player - 1] += 1
    print(scores_list)

def reviewAnsers(player_dict):
    question = timedInput("Would you like to review player answers? 'y/n': ", timeout=-1, allowCharacters="y, n")
    for player in range(1, 3):
        score = 0
        print(f"---------- Player: {player} ----------")
        for round in range(game_settings()[0]):
            roundpoints = 0
            answer = player_dict[player][round][3]
            answer_letter1 = player_dict[player][round][3][0]
            category = player_dict[player][round][1]
            letter = player_dict[player][round][2]
            if answer_letter1 == letter:
                if answer in category_dict[f"{category}"]:
                    roundpoints = 1
            print(f"Round: {round + 1}\nCategory: {category}\nAnswer: {answer}\nPoints Earned: {roundpoints}\n")





get_files()

def main():
    files = get_files()
    check_files(files[0], files[1])
    player_dictionary = genrateplayerdict(files[1])
    scoreGame(player_dictionary, files[1])
    reviewAnsers(player_dictionary)


main()