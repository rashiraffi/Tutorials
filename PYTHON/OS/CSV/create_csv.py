import csv
data=[['apple','iphone','us'],['microsoft','windows','us'],['google','pixel','us']]
with open("demo.csv","w") as file:
    writer = csv.writer(file)   #calling writer function of csv mod with this csv file as parameter
    # Writer var is now a instance of a csv writer class. There are two functions
    # writerow and writerows.
    writer.writerows(data)      # Since we have all the data in "Data" variable writerows function is used