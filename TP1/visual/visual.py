import os, time

file = open('../visual/map3-intent.txt')
file_content = file.read()
file_split = file_content.split("&&")
for frame in file_split:
     print(frame)
     time.sleep(0.3)
     os.system('clear')
