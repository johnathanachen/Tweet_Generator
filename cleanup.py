from string import punctuation

class Clean():
    """ Returns a list of single words """

    def __init__(self):
        pass

    def _remove_punctuation(self, file_name):
        """ Remove all punctuation from text file """
        with open(file_name, 'r') as myfile:
            dialouge_list = myfile.read()
        long_string = ''.join(dialouge_list)
        long_string = ''.join(c for c in long_string if c not in punctuation)
        return long_string

    def _single_words(self, long_string):
        """ Seperate string into word list """
        word_list = long_string.split()
        return word_list

    def clean_text(self, file_name):
        long_string = self._remove_punctuation(file_name)
        word_list = self._single_words(long_string)
        return word_list

# file_name = "transcript.txt"
# Clean(file_name)
