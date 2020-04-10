import csv
car = [{"name":"Urus","year":2019,"BHP":478,"comapny":"Lamborgini"},{"name":"911 Turbo S","year":2019,"BHP":400,"comapny":"Porshe"},{"name":"La Feerrari","year":2018,"BHP":950,"comapny":"Ferrari"}]
keys = ["name","year","BHP","comapny"]
with open("cars.csv","w") as cars:
    writer = csv.DictWriter(cars,fieldnames=keys)
    writer.writeheader()        #this will write first line of the csv based on the keys given
    writer.writerows(car)       #this will turn the list of dict to line in the file