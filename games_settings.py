# comment check
from pathlib import Path

categories = {}
start_letters = {}

csv_folder = Path("CSV_folder")
category_csvs = [csv_folder / "fruits.csv", csv_folder / "presidents.csv", csv_folder / "countries.csv"]

def game_settings(rounds: int = 3, ):
    rounds = input("How many rounds do you want to play?")
    players = input("How many players are there?")
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


def main():
    pass

    # create_categories(category_csvs, categories)
    # generate_start_letters(categories, start_letters)


if __name__ == "__main__":
    main()



