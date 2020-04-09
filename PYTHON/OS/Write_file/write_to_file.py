with open("demo.txt","w") as file:          # "w" means open the file in write mode(write only)[Can't read]
    file.write("This is a demo file...")    # if file here ("dewmo.txt") doesn't exist then
    file.write("this is second line")       # python will create it
                                            # if the file does exist, then its current contents will
                                            # be overwritten
    
with open("demo.txt","a") as file:          # "a" means open file in append mode. The file show already exist
    file.write("This is second line")       # write function will append the content to the file

with open("demo.txt") as file:
    print(file.read())