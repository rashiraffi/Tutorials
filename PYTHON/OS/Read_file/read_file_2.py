with open("demo.txt") as file:
    for line in file:
        print(line.upper())

with open("demo.txt") as file:
    for line in file:
        print(line.strip().upper())