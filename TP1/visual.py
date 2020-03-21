import os, time
import sys

file = open(sys.argv[1])
file_content = file.read()
file_split = file_content.split("&&")
for frame in file_split:
     print(frame)
     time.sleep(0.3)
     os.system('clear')
