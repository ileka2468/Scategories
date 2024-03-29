# comment check
from pathlib import Path
import random
from pytimedinput import timedInput
from art import*



'''
initializes two empty maps that will hold category data loaded in from the CSV files, where the key is a slice of the
file name prior to the extension name and the data WILL be a list of values read in from the CSV.
'''
#
categories = {}
start_letters = {}

csv_folder = Path("CSV_folder")
category_csvs = [csv_folder / "Fruits.csv", csv_folder / "Presidents.csv", csv_folder / "Countries.csv",
                 csv_folder / "Food.csv", csv_folder / "3 letter words.csv",
                 csv_folder / "Active NBA Players.csv", csv_folder / "Active NFL Players.csv",
                 csv_folder / "Languages.csv", csv_folder / "Celebrities.csv", csv_folder / "Zoo Animals.csv",
                 csv_folder / "NBA Teams.csv", csv_folder / "Netflix Titles.csv", csv_folder / "US Cities.csv",
                 csv_folder / "Vegetables.csv", csv_folder / "Video Games.csv"]

# function that writes game info into a file, to be used later
def game_settings():
    with open("roundinfo.txt", "r") as f:
        line = f.readline()
        comma = line.find(",")
        rounds = line[:comma]
        players = line[comma + 1:]
    return (int(rounds), int(players))

# function that prompts the game creator on the settings for the game
def getdata():
    welcome = text2art("Scattergories  Menu")
    print(welcome)
    while True:
        roundz, timeout1 = timedInput("How many rounds per game?: ", timeout=-1, allowCharacters="1,2,3,4,5,6,7,8,9,0")
        playerz, timeout2 = timedInput("How many people will be playing: ", timeout=-1, allowCharacters="1,2,3,4,5,6,7,8,9,0")
        if int(roundz) > 0 and int(playerz) > 0:
            break
        else:
            print("****Your round number and player must be greater than 0****\n\n")
    print("\nYour game settings have been save you can now play the game by running PlayGame.py!")

    with open("roundinfo.txt","w") as f:
        f.write(f"{roundz},{playerz}")


'''
loops through the csv list and opens each CSV and reads the data into the map created above where the key is the file
name prior to the period and the value is a list of the data being read in from the CSV file.
'''

def create_categories():
    for csv in category_csvs:
        with open(csv, "r", errors="ignore") as f:
            period = str(csv).find(".")
            slash = str(csv).find("\\") + 1
            csv = str(csv)[slash:period]
            categories[str(csv)] = []
            next(f)
            for line in f:
                item = line.split(",")[0].strip()
                categories[csv].append(item.replace('"', ""))
    return categories

'''
function that loops through the keys and values in the category list and generates a dictionary that maps the category
name to a valid list of starting letters by, taking the dictionary value which is a list and converting it into a set
which removes all duplicates.
'''

def generate_start_letters():
    for category_key, category_items in categories.items():
        start_letters[category_key] = set()
        for item in category_items:
            start_letters[category_key].add(item[0])

    return start_letters
'''
writes the settings file by choosing random categories for each round and writing the information to a file that, the 
game module will need to play the rounds.
'''

def write_settingsFile(categories, letters):
    with open("settings.txt", "w") as f:
        f.write(f"Expected Players: {game_settings()[1]}\n")
        for round in range(game_settings()[0]):
            category = random.choice(list(categories.keys()))
            letter = random.choice(list(letters[category]))
            f.write(f"{round}, {category}, {letter}\n")


def main():
    getdata()
    categoriess = create_categories()
    letters = generate_start_letters()
    write_settingsFile(categoriess, letters)

    # create_categories(category_csvs, categories)
    # generate_start_letters(categories, start_letters)


if __name__ == "__main__":
    main()



