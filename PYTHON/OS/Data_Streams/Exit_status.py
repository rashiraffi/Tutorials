#!/usr/bin/env python3
import os
import sys
filename=sys.argv[1]

if not os.path.exists(filename):
    with open(filename,"w") as f:
        f.write("New file Created\n")
else:
    print("Error, the file {} already exists!".format(filename))
    sys.exit(1)

"""
rashi@rr:   Tutorial/PYTHON/OS/Data_Streams$ ./Exit_status.py demo.txt
rashi@rr:   Tutorial/PYTHON/OS/Data_Streams$ echo $?
0
rashi@rr:   Tutorial/PYTHON/OS/Data_Streams$ ./Exit_status.py demo.txt
Error, the file demo.txt already exists!
rashi@rr:   Tutorial/PYTHON/OS/Data_Streams$ echo $?
1
rashi@rr:   Tutorial/PYTHON/OS/Data_Streams$ 
"""