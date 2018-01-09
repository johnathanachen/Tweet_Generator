import random


class HistogramWithCount:

    def __init__(self):
        """ Initialize the data """
        self.nodes = []
        self.word_count = 0

    def __len__(self):
        """ Gets the amount of words in the data set. Not types! """
        return self.word_count

    def __str__(self):
        """ THe string representation of the nodes """
        return str(self.nodes)#!python
from __future__ import division, print_function
import random

class Dictogram(dict):

    def __init__(self, iterable=None):
        """Initialize this histogram as a new dict; update with given items"""
        super(Dictogram, self).__init__()
        self.types = 0  # the number of distinct item types in this histogram
        self.tokens = 0  # the total count of all item tokens in this histogram
        if iterable:
            self.update(iterable)

    def update(self, iterable):
        """Update this histogram with the items in the given iterable"""
        for item in iterable:
            # TODO: increment item count
            self.tokens += 1
            if item in self:
                self[item] += 1
            else:
                self[item] = 1
        self.types = len(self)

    # def count(self, item):
    #     """Return the count of the given item in this histogram, or 0"""
    #     # TODO: retrieve item count
    #     return self.get(item, 0)

    # def return_random_word(self):
    #     # Another way:  Should test: random.choice(histogram.keys())
    #     random_key = random.sample(self, 1)
    #     print(random_key[0])
    #     return random_key[0]

    def return_weighted_random_word(self):
        # Step 1: Generate random number between 0 and total count - 1
        random_int = random.randint(0, self.tokens-1)
        index = 0
        list_of_keys = list(self.keys())
        # self.types

        # print 'the random index is:', random_int
        # for i in range(0, list_of_keys):
        for key in list_of_keys:
            index += self[key]
            # print index
            if(index > random_int):
                # print(list_of_keys[i])
                return key

if __name__ == '__main__':
    dict = {'one': 1, 'fish': 4, 'two': 1, 'red': 1, 'blue': 1}
    D = Dictogram(dict)

    def update_word(self, word):
        """ If the word is already in the histogram we will update the number of times the word occurs. If not then
        we insert it into our nodes

        :param word:     The word we want update in the data set
        """

        self.word_count += 1
        length = len(self.nodes)

        # If we have no data. Let's just create a new node.
        if length < 1:
            self.nodes.append([1, [word]])
            return

        for i in range(length):
            current_node = self.nodes[i]
            words = current_node[1]

            # If our word is in the current node. Remove it then check more things.
            if word in words:
                words.remove(word)

                # If there are no following nodes. We are the greatest node and can just add a new node
                if i > length - 2:
                    self.nodes.append([current_node[0] + 1, [word]])
                else:
                    next_node = self.nodes[i + 1]

                    # If the next nodes occurrences is equal to one more then the current node. We add our word to the
                    # next node. If not, then we create a new node there.
                    if next_node[0] == current_node[0] + 1:
                        next_node[1].append(word)
                    else:
                        self.nodes.insert(i + 1, [current_node[0] + 1, [word]])

                # If there are no words left in this node. We delete the node.
                if len(words) < 1:
                    del self.nodes[i]

                return

        # We check if the first nodes occurrences is 1. If it is we add our word. If not, we create a new node that
        # the occurrences is one
        if self.nodes[0][0] == 1:
            self.nodes[0][1].append(word)
        else:
            self.nodes.insert(0, [1, [word]])

    def random_word(self):
        """ Gets a random word from the histogram

        :return:    The random word
        """

        number = random.random()
        word_count = self.word_count
        last_percent = 0
        for node in self.nodes:
            last_percent = frequency = last_percent + node[0] * len(node[1]) / word_count

            # If the number is greater then the percentage we calculated before, then this is the random node we want.
            # Then we get a random word from the node's second index which is the list of words
            if number < frequency:
                return node[1][random.randint(0, len(node[1]) - 1)]


class Histogram:

    def __init__(self):
        """ Initialize the data """
        self.nodes = {}
        self.word_count = 0

    def __len__(self):
        """ Gets the amount of words in the data set. Not types! """
        return self.word_count

    def __str__(self):
        """ THe string representation of the nodes """
        return str(self.nodes)

    def update_word(self, current_word):
        """ If the word is already in the histogram we will update the number of times the word occurs. If not then
        we insert it into our nodes

        :param current_word:     The word we want update in the data set
        """

        self.word_count += 1

        if current_word in self.nodes:
            self.nodes[current_word] += 1
        else:
            self.nodes[current_word] = 1

    def random_word(self):
        """ Gets a random word from the histogram

        :return:    The random word
        """

        random_range = random.random()
        total_word_count = self.word_count
        last_percent = 0

        # Go through all our words checking if the one is coming up
        for current_word in self.nodes:
            word_occurrences = self.nodes[current_word]

            # We get the frequency of the word
            last_percent = frequency = last_percent + word_occurrences / total_word_count

            # If the number is greater then the percentage we calculated before, then this is the random node we want.
            if random_range < frequency:
                return current_word

    def __repr__(self):
        return "Histogram[" + str(self.nodes) + "]"


if __name__ == "__main__":
    data = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']

    gram = Histogram()
    for word in data:
        gram.update_word(word)

    dd = {}

    for i in range(10000):
        letter = gram.random_word()

        if letter in dd:
            dd[letter] += 1
        else:
            dd[letter] = 1

    print(dd)
