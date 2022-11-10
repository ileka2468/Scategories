with open("holidays.csv", "r") as f:
    good = set()
    for line in f:
        line = line.strip()
        if line == "Additional Day":
            pass
        else:
            good.add(line)

with open("new.csv", "w") as f2:
    for holiday in good:
        f2.write(f"{holiday}\n")
