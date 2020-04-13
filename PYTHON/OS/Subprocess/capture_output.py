#!/usr/bin/env python3
import subprocess
result = subprocess.run(["host","8.8.8.8"], capture_output=True)
print(result.returncode)
print(result.stdout)

result = subprocess.run(["rm","doest_not_exist"],capture_output=True)
print(result.stdout)
print(result.stderr)
