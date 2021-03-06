import os

def getwordfreqs(filename):
    """ Returns a dictionary with each used word and the frequency of the word

    Arguments:
    filename -- name of the file formatted in string, i.e. "page2.txt"
    """

    wordDictionary = {}
    with open(__getFileDirectory(filename)) as f:
        for line in f:
            for word in line.split():
                if word.lower() in wordDictionary:
                    wordDictionary[word.lower()] += 1
                else:
                    wordDictionary[word.lower()] = 1
    return wordDictionary

def getwordsline(filename, word):
    """ Returns a list of line numbers where the given word is used

    Arguments:
    filename -- filename -- name of the file formatted in string, i.e. "page2.txt"
    word -- a word formatted in string
    """

    lineCounter = 0
    lineList = []
    with open(__getFileDirectory(filename)) as f:
        for line in f:
            lineCounter += 1
            if word in line:
                lineList.append(lineCounter)

    return lineList

def __getFileDirectory(filename):
    """ Helper function that returns the directory of the given file

    Arguments:
    filename -- name of the file formatted in string, i.e. "page2.txt"
    """
    for dirName, subdirList, fileList in os.walk('.', topdown=False):
        if filename in fileList:
            return dirName + "/" + filename

if __name__ == "__main__":

    print(getwordfreqs("84-0.txt"))
    print(getwordsline("84-0.txt", "shall"))
