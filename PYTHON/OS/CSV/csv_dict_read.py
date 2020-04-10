import csv
with open("demo.csv") as companies:
    reader = csv.DictReader(companies)
    for row in reader:
        print(row)
        print("{} is located in {}".format(row["name"].upper(),row["country"].upper()))