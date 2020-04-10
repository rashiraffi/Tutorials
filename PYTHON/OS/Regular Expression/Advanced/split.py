import re
print(re.split(r"[.?!]","One sentence. Another one? And another last one!"))

print(re.split(r"([.?!])","One sentence. Another one? And another last one!"))

print(re.sub(r"[\w.%+-]+@[\w.-]+","[REDACTED]", "Received an email for go_nuts95@my.example.com"))

# we'd use parentheses to create capturing groups. In the first parameter, we've got an expression that 
# contains the two groups that we want to match: one before the comma and one after the comma. We want 
# to use a second parameter to replace the matching string. We use backslash two to indicate the second 
# captured group followed by a space and backslash one to indicate the first captured group

print(re.sub(r"^([\w .-]*), ([\w .-]*)$",r"\2 \1", "Lovelace, Ada"))