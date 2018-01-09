from __future__ import division, print_function  # Python 2 and 3 compatibility
from nltk.tokenize import sent_tokenize
from scripts.dictogram import *

class Markov(dict):
    """Markov is a dictionary of key(current word), val/next_word(dictogram). Takes a string of text"""
    def __init__(self, text=None):
        #Create start and stop dictogram to store the begging of words and end of words
        self['START'] = Dictogram()
        if text:
            #Creating a markov model for each sentence
            self.markov(text, 1)
    def tokenize_sentence(self, text):
        """ Using nltk split corpus based on sentences"""
        sentence_arr = sent_tokenize(text)
        # print("There are {} sentences".format(len(sentence_arr)))
        return sentence_arr



    def markov(self,text, order=1):
        """ Create a markoff model based on the text array input into the file """
        corpus = self.tokenize_sentence(text)
        # print(corpus)
        x = 0
        for sentence in corpus:
            sentence = sentence.split()
            x = 0
            self['START'].add_count(sentence[0])
            # From the first to the to last word
            while x< len(sentence)-order:
                word = " ".join(sentence[x:x+order])
                next_word = sentence[order+x]
                if word not in self.keys():
                    self[word]= Dictogram()
                self[word].add_count(next_word)
                x+=1
            # Adding a stop token to the final word
            self[sentence[-1]] = Dictogram()
            self[sentence[-1]].add_count('STOP')

    def weight_markov(self):
        """ Return a key with a value of possible next words weight """
        markov_weight = {}
        for key, val in self.items():
            markov_weight[key] = weighted_hist(val)
        return markov_weight

    def generate_sentence(self, length=10):
        """Return a sentence based on markov model"""
        sentence = ""
        weights = self.weight_markov()
        #Get First word
        word = stochastic_sampling(weights['START'])
        sentence += word
        words = 1
        while words <= length:
            word = stochastic_sampling(weights[word])
            if word == 'STOP':
                break
            sentence += " "+word
        print(sentence)
        return sentence



def main():
    file_name = open("cleaned_corpus.txt", "r")
    read_file = file_name.read()
    marky = Markov(read_file)
    weighted_markov = marky.weight_markov()
    sentence = marky.generate_sentence()

main()
