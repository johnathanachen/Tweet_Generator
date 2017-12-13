import os

from flask import Flask, render_template
from random import randint
from scripts.markov import MarkovChain
import random

app = Flask(__name__)

file_name = "cleaned_corpus.txt"

@app.route('/', methods=['GET', 'POST'])
def hello():
    model = MarkovChain(file_name, 3)
    try:
        sentence = model.generate_sentence()
    except TypeError:
        sentence = model.generate_sentence()
    count = read_current_count()
    new_count = write_new_count()
    reset = reset_score()
    score = read_score()
    return render_template("index.html", sentence=sentence, count=count, score=score)

######################################################
# Increase click counter
######################################################

def read_current_count():
    '''
    Read increased count from file
    '''
    text_file = open("data/counter.txt", "r")
    count = text_file.read()
    return count

def write_new_count():
    '''
    Write increased count to file
    '''
    f = open("data/counter.txt", "r")
    data = f.read()
    new_count = int(data) + 1
    string_format = str(new_count)
    f = open("data/counter.txt", "w")
    f.write(string_format)


######################################################
# Add, subtract, Read score
######################################################

@app.route('/add_score', methods=['GET', 'POST'])
def add_to_score():
    '''
    Add more score to file
    '''
    f = open("data/current_score.txt", "r")
    score = f.read()
    new_count = int(score) + 10
    string_format = str(new_count)
    f = open("data/current_score.txt", "w")
    f.write(string_format)
    new_score = read_score()
    return new_score

@app.route('/minus_score', methods=['GET', 'POST'])
def subtract_score():
    '''
    Add more score to file
    '''
    f = open("data/current_score.txt", "r")
    score = f.read()
    new_count = int(score) - 10
    string_format = str(new_count)
    f = open("data/current_score.txt", "w")
    f.write(string_format)
    new_score = read_score()
    return new_score

@app.route('/read_score', methods=['GET', 'POST'])
def read_score():
    '''
    Read score from file
    '''
    f = open("data/current_score.txt", "r")
    score = f.read()
    return score

def reset_score():
    '''
    Add more score to file
    '''
    f = open("data/current_score.txt", "r")
    score = f.read()
    new_count = 0
    string_format = str(new_count)
    f = open("data/current_score.txt", "w")
    f.write(string_format)
    new_score = read_score()
    return new_score

######################################################
# Check if guess is right or wrong
######################################################

def read_current_guess():
    '''
    Read guess token from file
    '''
    text_file = open("data/guess_token.txt", "r")
    guess_state = text_file.read()
    return guess_state

def write_new_guess(guess):
    '''
    Write new guess to file
    '''
    f = open("data/guess_token.txt", "w")
    f.write(guess)

######################################################
# Pick new text to show
######################################################

@app.route('/pick_text', methods=['GET', 'POST'])
def pick_text():
    '''
    Chooses to pick real or fake text before showing it to the user
    '''
    random_number = randint(1,4)
    if random_number == 1:
        f = open("real_tweets.txt", "r")
        tweets = f.read()
        tweet_list = tweets.splitlines()
        for i in tweet_list:
            if len(i) == 0 or i == "...":
                tweet_list.remove(i)
        results = random.choice(tweet_list)
        write_new_guess("True")
        return results
    else:
        # f = open("transcript.txt", "r")
        # data = f.read()
        model = MarkovChain(file_name, 3)
        try:
            sentence = model.generate_sentence()
        except TypeError:
            sentence = model.generate_sentence()
        write_new_guess("False")
        return sentence

@app.route('/correct_guess', methods=['GET', 'POST'])
def correct_guess():
    guess_state = read_current_guess()
    return guess_state


######################################################
# Add counter and update UI
######################################################

@app.route('/new_count', methods=['GET', 'POST'])
def new_count():
    count = read_current_count()
    new_count = write_new_count()
    return count + " retweets"


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
