# comment check
from pathlib import Path
import random

categories = {}
start_letters = {}

csv_folder = Path("CSV_folder")
category_csvs = [csv_folder / "fruits.csv", csv_folder / "presidents.csv", csv_folder / "countries.csv"]

def game_settings():
    rounds = 6
    players = 2
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



