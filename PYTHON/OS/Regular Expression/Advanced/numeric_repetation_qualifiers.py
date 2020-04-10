import re
print(re.search(r"[a-zA-Z]{5}", "a ghost"))
result = re.search(r"[a-zA-Z]{5}", "a scary ghost")
print(result)

result = re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared")
print(result)


result = re.findall(r"\b[a-zA-Z]{5}\b", "a scary ghost appeared")
print(result)

result = re.findall(r"\w{5,10}", "I really like strawberries")
print(result)

result = re.findall(r"\b\w{5,10}\b", "I really like strawberries")
print(result)

result = re.findall(r"\w{5,}", "I really like strawberries")
print(result)

result = re.search(r"s\w{,20}", "I really like strawberries")
print(result)