import os

#   Create file "demo.txt"

with open("demo.txt","w") as file:
    file.write("This is a demo file...")
print("demo.txt file created")

print(os.path.getsize("demo.txt"))

print(os.path.getmtime("demo.txt")) #   it will return unix timestamp, It represents the number of seconds 
                                    #   since JAN 01 1970.

import datetime
timestamp=os.path.getmtime("demo.txt")
print(datetime.datetime.fromtimestamp(timestamp))

#   print absolute path
print(os.path.abspath("demo.txt"))