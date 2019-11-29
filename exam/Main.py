import os
import re
import glob

"""

Sorts files in the folder /files

"""

class FileManager(object):

    @classmethod
    def _change_directory(cls, filename):
        """
        Helper function that returns the directory of the given file,
         given that it is in the current working directory's subdirectory
        :param filename: Filename formatted in string, i.e "page2.txt"
        :return: Null
        """
        for dirName, _, fileList in os.walk('.'):
            if filename in fileList:
                return dirName + "/" + filename

    def list_files(self, filename="."):
        """
        :return: An array of all files and folders in current working directory
        """
        file_array = []

        for _, sub_directory, file_list in os.walk(filename):
            file_array += file_list
            file_array += sub_directory

        return file_array


    def graphic_files_list(self):
        """
        :return: An array of all graphics files
        """
        file_array = []
        extensions = ["eps", "tif", "png", "jpg"]

        for _, sub_directory, file_list in os.walk('./files'):
            for file in file_list:
                if file.split(".")[-1] in extensions:
                    file_array.append(file)

        return file_array

    def search_tex(self, filename):
        """
        :param filename: Filename formatted in string, i.e "introduction0old.tex"
        :return: array with graphic filenames in directory that are also mentioned in the given .tex file
        """
        graphic_files = self.graphic_files_list()
        temp_graphic_files = {}
        filename_list = []

        # Saves all filenames without extensions
        for file in graphic_files:
            temp_graphic_files[file.split(".")[0]] = file

        with open(self._change_directory(filename)) as f:
            for line in f:
                # Ignores comments
                if line[0] == '%':
                    continue
                for word in line.split():
                    # Removes all special characters from word
                    word_cleaned = re.sub(r'[^\w]', ' ', word)
                    arr = word_cleaned.split(" ")
                    for x in arr:
                        if x in temp_graphic_files:
                            # Assigns filename with full filename with extension in temp_graphic_files dictionary
                            filename_list.append(temp_graphic_files[x])
        return filename_list

    def clean_text_directory(self, filename):
        """
        Moves non-graphic files that are not included in the .tex file to a folder called dump. .bib files are not moved
        Prints how many graphic files were found and how many were moved into their respective folders
        :return: None
        """

        graphic_files = self.graphic_files_list()
        graphic_extensions = []
        file_list = self.list_files()
        tex_files = self.search_tex(filename)
        os.chdir("files")

        # Finds all graphics extension found in files folder
        for file in graphic_files:
            extension = file.split(".")[-1]
            if extension not in graphic_extensions:
                graphic_extensions.append(extension)

        # Create dump folder if it doesnt exist
        if not os.path.exists("dump"):
            os.mkdir("dump")

        # Makes a directory for every graphics extension
        counter = 0
        for filename in graphic_files:
            counter += 1
            extension = filename.split(".")[-1].lower()
            if not os.path.exists(extension):
                os.mkdir(extension.lower())

        # Moves all graphics files into their respective folders
        print("{} graphics files were found".format(counter))
        for extension in graphic_extensions:
            counter = 0
            for _ in glob.glob("*." + extension):
                counter += 1

            command = "mv *.{} {}".format(extension, extension)
            os.system(command)
            print("{} files were moved to the {} folder".format(counter, extension))

        # Makes a list of the remaining files
        files = []
        for dirName, _, fileList in os.walk('.'):
            files = fileList
            break
        # Move all files dont end with .tex or .bib to dump folder
        for filename in files:
            extension = filename.split(".")[-1]
            if extension != "tex" and extension != "bib":
                if os.path.exists(filename) and os.path.isfile(filename):
                    command = "mv {} dump".format(filename)
                    os.system(command)



if __name__ == "__main__":
    fm = FileManager()
    print(fm.list_files("./files"))
    print(fm.graphic_files_list())
    print(fm.search_tex("introduction-old.tex"))
    print(fm.search_tex("GSGradientFromColor.tex"))
    fm.clean_text_directory("GSGradientFromColor.tex")
