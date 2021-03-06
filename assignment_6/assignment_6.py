import os
import re

def sortFileByWords(filename):
	""" Sorts a .txt file by words both lexiographically and by word length

	Arguments:
	filename -- name of the file formatted in string, i.e. "page2.txt"
	"""

	sortList = []

	#Fills sortList with words devoid of special characters from given .txt file
	with open(__getFileDirectory(filename)) as f:
		for line in f:
			for word in line.split():
				#Removes characters from the word with regular expressions
				res = re.sub(r'[^\w]', '', word)
				sortList.append(res)

	#Sorts list by length with selection sort
	for fillslot in range(len(sortList) - 1, 0, -1):
	   positionOfMax = 0
	   for location in range(1, fillslot + 1):
		   if len(sortList[location]) > len(sortList[positionOfMax]):
			   positionOfMax = location
	   sortList[fillslot], sortList[positionOfMax] = sortList[positionOfMax], sortList[fillslot]

	#Sorts any strings with equal length, lexiographically with bubblesort
	for elem in range(len(sortList) - 1, 0, -1):
		for i in range(elem):
			if len(sortList[i]) == len(sortList[i + 1]):
				""" Turns the characters in the string into a unicode point
					and is then joined together as one larger integer value
				"""
                                if sortList[i] > sortList[i + 1]:
					sortList[i], sortList[i + 1] = sortList[i + 1], sortList[i]
	return sortList

def __getFileDirectory(filename):
	""" Helper function that returns the directory of the given file

	Arguments:
	filename -- name of the file formatted in string, i.e. "page2.txt"
	"""
	for dirName, subdirList, fileList in os.walk('.', topdown=False):
		if filename in fileList:
			return dirName + "/" + filename

if __name__ == '__main__':
	print(sortFileByWords("random.txt"))

