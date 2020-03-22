from collections import deque

class ConfigFileReader():
    def __init__(self, configFileName):
        file = open(configFileName)
        file_content = file.readlines()
        settings = {}
        selected = False
        for line in file_content:
            mylist = deque(line.rstrip().split(" "))
            name = mylist.popleft()
            current = settings[name] = mylist.pop() == '1'
            if name not in ['PrintState', 'CornerSense', 'H']:
                selected = current
            elif selected and current:
                print("Please select only one method")
                exit(1)
        self.settings = settings
    
    def getSettings(self):
        return self.settings