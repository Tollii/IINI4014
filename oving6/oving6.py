import os
import re

def sortFileByWords(filename):
	""" Sorts a list of strings lexiographically and by length
		
	Arguments:
	filename -- name of the file formatted in string, i.e. "page2.txt"
	"""

	sortList = []

	#Changes directory and fills sortList with all words contained in the file
	os.chdir(__getFileDirectory(filename))
	file = open(filename, "r")
	if file.mode == "r":
		lineArray = file.readlines()
		for line in lineArray:
			for word in line.split():
				sortList.append(word)

	# Removes all non-alphanumerical characters
	for i in range(len(sortList)):
		sortList[i] = re.sub(r'[^\w]', '', sortList[i])


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
				w1 = int(''.join(str(ord(c)) for c in sortList[i]))
				w2 = int(''.join(str(ord(c)) for c in sortList[i + 1]))
				if w1 > w2:
					sortList[i], sortList[i + 1] = sortList[i + 1], sortList[i]				
	return sortList

def __getFileDirectory(filename):
	""" Helper function that returns the directory of the given file

	Arguments:
	filename -- name of the file formatted in string, i.e. "page2.txt"
	"""
	for dirName, subdirList, fileList in os.walk('.', topdown=False):
		if filename in fileList:
			return dirName

if __name__ == '__main__': 
	print(sortFileByWords("random.txt"))

