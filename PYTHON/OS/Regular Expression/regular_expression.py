import re
print(re.search(r"A.*a","Argentina"))

print(re.search(r"^A.*a$","Azerbaijan"))

print(re.search(r"^A.*a$","Australia"))

pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
print(re.search(pattern,"This_is_a_valid_variable"))

print(re.search(pattern,"thsi is not a valid varible name"))

print(re.search(pattern,"m1"))

print(re.search(pattern,"2m"))