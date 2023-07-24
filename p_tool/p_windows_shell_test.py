import subprocess
import os
import json

cmd_set = "set"

p = subprocess.Popen(args=cmd_set,stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True)

stdout,stderr = p.communicate()
print(stdout.decode('utf-8'))

print(os.system("set"))