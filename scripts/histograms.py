#!python
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
