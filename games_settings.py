def create_categories(csv_list, categories):
    for csv in csv_list:
        with open(csv, "r") as f:
            period = csv.find(".")
            csv = csv[:period].capitalize()
            categories[csv] = []
            next(f)
            for line in f:
                item = line.split(",")[0].strip()
                categories[csv].append(item)

    print(categories)

def main():
    categories = {}
    category_csvs = ["fruits.csv", "presidents.csv", "countries.csv"]
    create_categories(category_csvs, categories)


if __name__ == "__main__":
    main()



