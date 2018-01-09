from scripts.histogram import Dictogram
import random
from collections import deque
import re
#yeah
class Markov():

    def __init__(self):
        pass

    def _markov_chain(self, data):
        """ Markov model """
        #Dictionary that stores windows as the key in the key-value pair and then the value
        #for each key is a dictogram
        markov_chain = dict()
        # Looping through the ammount of indexs in the list
        for index in range(0, len(data) - 1):
            # If index word of list exists in dictionary then update the current index
            # Store a histogram of words for each window
            if data[index] in markov_chain:
                markov_chain[data[index]].update([data[index + 1]])
            else:
                markov_chain[data[index]] = Dictogram([data[index + 1]])
        return markov_chain

    # Walk our model
    def _generate_random_start(self, model):
        # Generate a "valid" starting word.
        # A valid starting word are words that start a sentence
        return random.choice(list(model.keys()))

    # Generating sentence using first order markov_model
    def _generate_sentence(self, length, markov_model):
        # length parameter is length of the sentence
        # Create first word
        current_word = self._generate_random_start(markov_model)
        # Save first word to sentence list
        sentence = [current_word]
        # Loop through the length of sentence provided
        for i in range(0, length):
            # Getting current dictogram and starting from the current word(first word)
            current_dictogram = markov_model[current_word]
            # Getting random word from dictogram starting from the place of the current word
            random_word = current_dictogram.return_weighted_random_word()
            # Setting current word variable to the random word
            current_word = random_word
            # Append the new current word until the sentence length is formed
            sentence.append(current_word)
        sentence[0] = sentence[0].capitalize()
        sentence = ' '.join(sentence) + '.'
        return sentence

    def main(self, data, length):
        markov_chain = self._markov_chain(data)
        sentence = self._generate_sentence(length, markov_chain)
        return sentence

# data = ["how", "much", "wood", "would", "a", "wood", "chuck", "chuck", "if", "a", "wood", "chuck", "could", "chuck", "wood"]
# Markov(data, 10)
