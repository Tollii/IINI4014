import os

def getwordfreqs(filename):


    wordDictionary = {}
    os.chdir(__getFileDirectory(filename))
    file = open(filename, "r")
    if file.mode == "r":
        lineArray = file.readlines()
        for line in lineArray:
            for word in line.split():
                if word.lower() in wordDictionary:
                    wordDictionary[word] += 1
                else:
                    wordDictionary[word] = 1





def getwordsline(filename, word):
    os.chdir(__getFileDirectory(filename))
    file = open(filename, "r")
    if file.mode == "r":
        lineArray = file.readlines()







def __getFileDirectory(filename):
    for dirName, subdirList, fileList in os.walk('.', topdown=False):
        print('Found directory: %s' % dirName)





__getFileDirectory("random.txt")
