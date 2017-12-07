#!python

from __future__ import division, print_function  # Python 2 and 3 compatibility


class Listogram(list):
    """Listogram is a histogram implemented as a subclass of the list type."""

    def __init__(self, word_list=None):
        """Initialize this histogram as a new list and count given words."""
        super(Listogram, self).__init__()  # Initialize this as a new list
        # Add properties to track useful word counts for this histogram
        self.types = 0  # Count of distinct word types in this histogram
        self.tokens = 0  # Total count of all word tokens in this histogram
        self.word_count = []
        # Count words in given list, if any
        if word_list is not None:
            self.add_count(word_list)

    def add_count(self, word_list, count=1):
        """Increase frequency count of given word by given count amount."""
        token = 0
        added_words = []
        for word in word_list:
            if word in self.word_count:
                self.tokens += 1
                self.word_count[word_element][1] += 1
                print("got it")
                print(self.word_count[word_element][1])
            else:
                word_element = [word]
                self.word_count.append(word_element)
                added_words.append(word_element)
                word_element.append(1)
                self.types += 1

        # print(self.word_count)
        return added_words

    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""
        if word in self.word_count:
            freq_value = self.word_count[word]
            return freq_value
        else:
            return 0

    def __contains__(self, word):
        """Return boolean indicating if given word is in this histogram."""
        if word in self.word_count:
            return True
        else:
            return False

    def _index(self, target):
        """Return the index of entry containing given target word if found in
        this histogram, or None if target word is not found."""
        does_contain = self.__contains__(target)
        index_of = list(self.word_count.keys()).index(target)
        if does_contain == True:
            return index_of
        else:
            None

def print_histogram(word_list):
    print('word list: {}'.format(word_list))
    # Create a listogram and display its contents
    histogram = Listogram(word_list)
    print('listogram: {}'.format(histogram.word_count))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
    for word in word_list[-2:]:
        freq = histogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()


def main():
    import sys
    arguments = sys.argv[1:]  # Exclude script name in first argument
    if len(arguments) >= 1:
        # Test histogram on given arguments
        print_histogram(arguments)
    else:
        # Test histogram on letters in a word
        word = 'abracadabra'
        print_histogram(list(word))
        # Test histogram on words in a classic book title
        fish_text = 'one fish two fish red fish blue fish'
        print_histogram(fish_text.split())
        # Test histogram on words in a long repetitive sentence
        woodchuck_text = ('how much wood would a wood chuck chuck'
                          ' if a wood chuck could chuck wood')
        print_histogram(woodchuck_text.split())


if __name__ == '__main__':
    x = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']
    Listogram(x)
