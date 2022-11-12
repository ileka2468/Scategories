# comment check
from pathlib import Path
import random

'''
This is a final project for CSC 241 at DePaul Univeersity, Professor: Tony Lowe, Group Members: William Ileka, Bakhodir Astanov, placeholder, placeholder
Project: Scategories
License: MIT 

Copyright 2022 William Ileka Et al.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


'''

categories = {}
start_letters = {}

csv_folder = Path("CSV_folder")
category_csvs = [csv_folder / "fruits.csv", csv_folder / "presidents.csv", csv_folder / "countries.csv"]

def game_settings():
    rounds = 2
    players = 6
    return (rounds, players)

def create_categories():
    for csv in category_csvs:
        with open(csv, "r") as f:
            period = str(csv).find(".")
            slash = str(csv).find("\\") + 1
            csv = str(csv)[slash:period].capitalize()
            categories[str(csv)] = []
            next(f)
            for line in f:
                item = line.split(",")[0].strip()
                categories[csv].append(item.replace('"', ""))

    return categories


def generate_start_letters():
    for category_key, category_items in categories.items():
        start_letters[category_key] = set()
        for item in category_items:
            start_letters[category_key].add(item[0])

    return start_letters


def write_settingsFile(categories, letters):
    with open("settings.txt", "w") as f:
        f.write(f"Expected Players: {game_settings()[1]}\n")
        for round in range(game_settings()[0]):
            category = random.choice(list(categories.keys()))
            letter = random.choice(list(letters[category]))
            f.write(f"{round}, {category}, {letter}\n")


def main():
    categoriess = create_categories()
    letters = generate_start_letters()
    write_settingsFile(categoriess, letters)

    # create_categories(category_csvs, categories)
    # generate_start_letters(categories, start_letters)


if __name__ == "__main__":
    main()



