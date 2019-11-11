import os


class TextAnalyzer:

    @classmethod
    def get_file_directory(cls, filename):
        """
        Helper function that returns the directory of the given file,
         given that it is in the current working directory's subdirectory
        :param filename: Filename formatted in string, i.e "page2.txt"
        :return: Null
        """
        for dirName, subdirList, fileList in os.walk('.'):
            if filename in fileList:
                return dirName + "/" + filename

    def get_word_frequency(self, filename):
        """
        :param filename: Filename formatted in string, i.e "page2.txt"
        :return: A dictionary with each used word and the frequency of the word
        """
        worddictionary = {}
        with open(self.get_file_directory(filename)) as f:
            for line in f:
                for word in line.split():
                    if word.lower() in worddictionary:
                        worddictionary[word.lower()] += 1
                    else:
                        worddictionary[word.lower()] = 1
        return worddictionary

    def get_paragraph_sentence_number(self, filename):
        """
        :param filename: Filename formatted in string, i.e "page2.txt"
        :return: Dictionary of paragraph number as key and number of sentences in the paragraph as value
        """
        punctuation = {'.', '!', '?'}
        paragraphdictionary = {}
        paragraphnum = 0

        with open(self.get_file_directory(filename)) as f:
            for line in f:
                if line == '\n':
                    continue
                if line[-1] == '\n':
                    paragraphnum += 1
                    for word in line.split():
                        if word[-1] in punctuation:
                            if paragraphnum in paragraphdictionary:
                                paragraphdictionary[paragraphnum] += 1
                            else:
                                paragraphdictionary[paragraphnum] = 1

                    # Adds a zero value if no punctuation is found in the paragraph
                    if paragraphnum in paragraphdictionary:
                        continue
                    else:
                        paragraphdictionary[paragraphnum] = 0

        return paragraphdictionary

    def get_percentage_easy(self, filename):
        """
        :param filename: Filename formatted in string, i.e "page2.txt"
        :return: Percentage of easy words
        """

    def get_percentage_unique(self, filename):
        """
        :param filename: Filename formatted in string, i.e "page2.txt"
        :return: A percentage of unique words. Unique words / total words
        """
        dictionary = self.get_word_frequency(filename)
        totalwords = 0
        uniquewords = 0

        for k, v in dictionary.items():
            totalwords += v
            uniquewords += 1

        return uniquewords / totalwords

    def get_words_line(self, filename, word):
        """
        :param filename: Filename formatted in string, i.e "page2.txt"
        :param word: word formatted in string
        :return: A list of line numbers where the given word is used
        """

        linecounter = 0
        linelist = []
        with open(self.get_file_directory(filename)) as f:
            for line in f:
                linecounter += 1
                if word in line:
                    linelist.append(linecounter)

        return linelist


if __name__ == "__main__":
    a = TextAnalyzer()
    print(a.get_paragraph_sentence_number("ransom.txt"))

