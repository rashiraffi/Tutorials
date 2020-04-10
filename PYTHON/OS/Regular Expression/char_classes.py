import re
print(re.search(r"[pP]ython","Python"))
print(re.search(r"[a-z]way","the end of the highway"))
print(re.search(r"[a-z]way","What a way to go"))
print(re.search(r".way","What a way to go"))

# match any character that aren;t in a group we use "^" this
# Any character that is not a letter

print(re.search(r"[^a-zA-Z0-9]","What a way to go"))

# If we want to match either one expression or another, we can use the pipe symbol to do that.
print("\nPipe\n")

print(re.search(r"cat|dog","I like cat"))

#   If we want to get all possible matches, we can do that using the findall function, which is also provided by the re module

print("\nFindall\n")

print(re.findall(r"cat|dog","I like cats and dogs"))
print(re.findall(r"cat|dog","I like cats and dogs and dogs"))