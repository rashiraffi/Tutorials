import re


print(re.search(r".com","welcome"))

print(re.search(r"\.com","welcome"))

print(re.search(r".com","www.google.com"))

print(re.search(r"\w*","This is an example"))       #\w = any letter number and _

print(re.search(r"\w*","This_is_not"))

#   \d for numbers, \s for space