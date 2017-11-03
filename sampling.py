from histo_dict import *
from random import randint

def pick_random_world():
    histrogram_results = list(histrogram(only_words))
    random_number = randint(0,len(histrogram_results))
    word = histrogram_results[random_number]
    return word

histrogram_list = histrogram(only_words)
word = pick_random_world()

def term_frequency(word, histrogram_list):
    time = histrogram_list[word] / len(histrogram_list)
    # print_out = print
    return(word, time)


# def pick_words(word1, word2, word3, word4)
#     pass

def run_sampling():
    pick_random_world()
    freq = str(term_frequency(word, histrogram_list))
    return freq



# pick 1,000 times and return the amount of time it shows up
