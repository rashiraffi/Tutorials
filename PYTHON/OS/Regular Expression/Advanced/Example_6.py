import re
#line = ["May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)","May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)","May 27 11:45:40 ubuntu.local ticky: ERROR: Error creating ticket [#1234] (username)"]
line = "May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [1234] (username)"
line1="Jan 31 00:21:30 ubuntu.local ticky: ERROR The ticket was modified while updating (breee)"
pattern=r"ticky: ([\w]+): ([\w ]+)\[\d+\] \((\w+)\)"
pattern1=r"ERROR ([\w ]+)"
result=re.search(pattern1,line1)
print(result)
print(result[1])
#print(result[1]+"\n"+result[2]+"\n"+result[3])