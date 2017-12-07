from random import randint
from donald_scrape import run_srape

""" PASS: Returns a random word """

def pick_random_world():
    word_list = run_srape()
    random_number = randint(0,len(word_list))
    word = word_list[random_number]
    # print(word)
    return word

# pick_random_world()
