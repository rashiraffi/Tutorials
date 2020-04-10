import csv
with open("cars.csv") as file:
    rows = csv.DictReader(file)
    for row in rows:
        print(row)