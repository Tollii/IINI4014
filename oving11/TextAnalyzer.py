import os
import re


class TextAnalyzer(object):

    @classmethod
    def change_directory(cls, filename):
        """
        Helper function that returns the directory of the given file,
         given that it is in the current working directory's subdirectory
        :param filename: Filename formatted in string, i.e "page2.txt"
        :return: Null
        """
        for dirName, _, fileList in os.walk('.'):
            if filename in fileList:
                return dirName + "/" + filename

    def get_words_line(self, filename, word):
        """
        :param filename: Filename formatted in string, i.e "page2.txt"
        :param word: word formatted in string
        :return: A list of line numbers where the given word is used
        """
        line_counter = 0
        line_list = []
        with open(self.change_directory(filename)) as f:
            for line in f:
                line_counter += 1
                if word in line:
                    line_list.append(line_counter)

        return line_list

    def get_word_frequency(self, filename):
        """
        :param filename: Filename formatted in string, i.e "page2.txt"
        :return: A dictionary with each used word as the key and the frequency of the word as the value
        """
        word_dictionary = {}
        with open(self.change_directory(filename)) as f:
            for line in f:
                for word in line.split():
                    word_cleaned = re.sub(r'[^\w]', '', word)
                    if word_cleaned.lower() in word_dictionary:
                        word_dictionary[word_cleaned.lower()] += 1
                    else:
                        word_dictionary[word_cleaned.lower()] = 1

        return word_dictionary

    def get_paragraph_sentence_number(self, filename):
        """
        :param filename: Filename formatted in string, i.e "page2.txt"
        :return: Dictionary of paragraph number as key and number of sentences in the paragraph as value
        """
        punctuation = {'.', '!', '?'}
        paragraph_dictionary = {}
        paragraph_num = 0

        with open(self.change_directory(filename)) as f:
            for line in f:
                if line == '\n':
                    continue
                if line[-1] == '\n':
                    paragraph_num += 1
                    for word in line.split():
                        if word[-1] in punctuation:
                            if paragraph_num in paragraph_dictionary:
                                paragraph_dictionary[paragraph_num] += 1
                            else:
                                paragraph_dictionary[paragraph_num] = 1

                    # Adds a zero value if no punctuation is found in the paragraph
                    if paragraph_num in paragraph_dictionary:
                        continue
                    else:
                        paragraph_dictionary[paragraph_num] = 0

        return paragraph_dictionary

    def get_sentence_length(self, filename):
        """
        :param filename: Filename formatted in string, i.e "page2.txt"
        :return: A dictionary with sentence numbers as keys, and number of words in the corresponding sentence as value
        """
        punctuation = {'.', '!', '?'}
        sentence_dictionary = {}
        word_counter = 0
        sentence_counter = 0
        with open(self.change_directory(filename)) as f:
            for line in f:
                if line == '\n':
                    continue
                for word in line.split():
                    word_counter += 1
                    if word[-1] in punctuation:
                        sentence_counter += 1
                        sentence_dictionary[sentence_counter] = word_counter
                        word_counter = 0

                # Handling of new line without punctuation, counts it as one sentence
                sentence_counter += 1
                if sentence_counter not in sentence_dictionary:
                    if word_counter == 0:
                        continue
                    sentence_dictionary[sentence_counter] = word_counter
                    word_counter = 0

        return sentence_dictionary

    def get_percentage_easy(self, filename):
        """
        :param filename: Filename formatted in string, i.e "page2.txt"
        :return: Percentage of easy words
        """
        dictionary = self.get_word_frequency(filename)
        number_of_words = self.get_number_of_words(filename)
        barrier = (number_of_words / 1000) * 1.3 + (number_of_words / (number_of_words * 0.8)) + 20
        easy_words = 0
        for _, v in dictionary.items():
            if v > barrier:
                easy_words += v

        return easy_words / number_of_words

    def get_percentage_difficult(self, filename):
        """
        :param filename: Filename formatted in string, i.e "page2.txt"
        :return: Percentage of difficult words
        """
        dictionary = self.get_word_frequency(filename)
        number_of_words = self.get_number_of_words(filename)
        barrier = (number_of_words / 1000) * 1.3 + (number_of_words / (number_of_words * 0.8)) + 20
        difficult_words = 0

        for _, v in dictionary.items():
            if v < barrier:
                difficult_words += v
        return difficult_words / number_of_words

    def get_percentage_unique(self, filename):
        """
        :param filename: Filename formatted in string, i.e "page2.txt"
        :return: A percentage of unique words. Unique words / total words
        """
        dictionary = self.get_word_frequency(filename)
        total_words = 0
        unique_words = 0

        for _, v in dictionary.items():
            total_words += v
            unique_words += 1

        return unique_words / total_words

    def get_number_of_words(self, filename):
        """
        :param filename: Filename formatted in string, i.e "page2.txt"
        :return: Number of words in the given file
        """
        word_counter = 0
        with open(self.change_directory(filename)) as f:
            for line in f:
                for _ in line.split():
                    word_counter += 1
        return word_counter


if __name__ == "__main__":
    a = TextAnalyzer()
    print(a.get_number_of_words("84-0.txt"))
    print(a.get_word_frequency("84-0.txt"))
    print(a.get_percentage_difficult('84-0.txt'))
