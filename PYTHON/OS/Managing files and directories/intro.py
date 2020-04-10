import os

#   Create file "demo.txt"

with open("demo.txt","w") as file:
    file.write("This is a demo file...")
print("demo.txt file created")

#   check whether the file exist or not for this path sub module of OS is used.
#   if the file exist the .exist function will return TRUE

print("demo.txt esist: ",os.path.exists("demo.txt"))

#   Rename file using .rename function

os.rename("demo.txt","demo_1.txt")

print("demo.txt esist: ",os.path.exists("demo.txt"))

print("demo_1.txt esist: ",os.path.exists("demo_1.txt"))

#   delete file using .remove function

os.remove("demo_1.txt")

print("demo_1.txt Deleted...")

print("demo_1.txt esist: ",os.path.exists("demo_1.txt"))