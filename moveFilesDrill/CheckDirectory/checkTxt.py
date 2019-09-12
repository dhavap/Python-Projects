import os
import time

fPath = 'C:\\Users\\Student\\Desktop\\Python Coding Projects\\CheckDirectory\\'

directory = os.listdir(fPath)

i=0
while i < len(directory):
    fName = directory[i]
    if  fName.endswith('.txt'): 
        abPath = os.path.join(fPath, fName)
        timeStamp = os.path.getmtime(abPath)
        convertTime = time.ctime(timeStamp)
        print("File Name: {} \nLatest date created/modified: {}\n".format(fName, convertTime))
    i+=1
