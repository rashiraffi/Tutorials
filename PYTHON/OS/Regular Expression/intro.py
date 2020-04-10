#!/usr/bin/env python
import re
result = re.search(r"aza","plaza")      # r indicate Rawstring
print(result)
result = re.search(r"aza","bazaar")      # r indicate Rawstring
print(result)
result = re.search(r"aza","maze")      # r indicate Rawstring
print(result)

print(re.search(r"^x","xenon"))
print(re.search(r"p.ng","penguin"))
print(re.search(r"p.ng","clapping"))
print(re.search(r"p.ng","sponge"))
print(re.search(r"p.ng","Pangaea"))
print(re.search(r"p.ng","Pangaea",re.IGNORECASE))