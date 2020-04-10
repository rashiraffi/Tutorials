import csv
f = open("demo.txt")    #open file
csv_f = csv.reader(f)
for row in csv_f:
    name,product,country=row
    print("Name: {}, Product: {}, Country: {}".format(name,product,country))
f.close()