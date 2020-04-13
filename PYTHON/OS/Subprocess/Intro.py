import subprocess

subprocess.run(["date"])

print(subprocess.run(["sleep","1"]))

result = subprocess.run(["ls","This_file_does_not_exist"])

print(result,"\n",result.returncode)