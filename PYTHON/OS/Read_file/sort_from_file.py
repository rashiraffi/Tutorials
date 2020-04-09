with open("demo_1.txt") as file:
    lines=file.readlines()
print(lines)
lines.sort()
print(lines)

with open("demo_1.txt") as files:
    for line in files.readlines():
        print(line.strip())