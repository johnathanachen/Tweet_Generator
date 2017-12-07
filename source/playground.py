from histograms import *
from collections import deque

def word_list():
    """ list of single words """
    # clean_text_list = clean_file('corpus.txt')
    clean_text_list = ["how", "much", "wood", "would", "a", "wood", "chuck", "chuck", "if", "a", "wood", "chuck", "could", "chuck", "wood"]
    return clean_text_list

def markov_chain(data):
    """ markov model for 1st order """
    #Dictionary that stores windows as the key in the key-value pair and then the value
    #for each key is a dictogram
    markov_chain = dict()
    # Looping through the amount of indexs in the list
    for index in range(0, len(data) - 1):
        # If index word of list exists in dictionary then update the current index
        # Store a histogram of words for each window
        if data[index] in markov_chain:
            markov_chain[data[index]].update([data[index + 1]])
        else:
            markov_chain[data[index]] = Dictogram([data[index + 1]])
    # print(markov_chain)
    return markov_chain

def main():
    data = word_list()
    markov_chain(data)

if __name__ == '__main__':
    main()
