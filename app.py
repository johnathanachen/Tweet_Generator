from flask import Flask, render_template
from random import randint
from cleanup import Clean
from markov import Markov
import random

app = Flask(__name__)

file_name = "transcript.txt"
data = Clean().clean_text(file_name)

@app.route('/', methods=['GET', 'POST'])
def hello():
    sentence = Markov().main(data, 10)
    guess_token = False
    count = read_current_count()
    new_count = write_new_count()
    return render_template("index.html", sentence=sentence, count=count)

def read_current_count():
    '''
    Read increased count from file
    '''
    text_file = open("counter.txt", "r")
    count = text_file.read()
    return count

def write_new_count():
    '''
    Write increased count to file
    '''
    f = open("counter.txt", "r")
    data = f.read()
    new_count = int(data) + 1
    string_format = str(new_count)
    f = open("counter.txt", "w")
    f.write(string_format)

def read_current_guess():
    '''
    Read guess token from file
    '''
    text_file = open("guess_token.txt", "r")
    guess_state = text_file.read()
    return guess_state

def write_new_guess(guess):
    '''
    Write new guess to file
    '''
    f = open("guess_token.txt", "w")
    f.write(guess)

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
        f = open("corpus.txt", "r")
        corpus = f.read()
        sentence = Markov().main(data, 10)
        write_new_guess("False")
        return sentence

@app.route('/correct_guess', methods=['GET', 'POST'])
def correct_guess():
    guess_state = read_current_guess()
    return guess_state

@app.route('/new_count', methods=['GET', 'POST'])
def new_count():
    count = read_current_count()
    new_count = write_new_count()
    return count + " retweets"

# @app.route('/correct_guess', methods=['GET', 'POST'])
# def correct_guess(guess):
#     if guess == True:
#         print("true")
#     else:
#         print("false")


# @app.route('/real_text', methods=['GET', 'POST'])
# def new_text():
#     sentence = Markov().main(data, 10)
#     return sentence

# @app.route('/fake_text', methods=['GET', 'POST'])
# def new_text():
#     sentence = Markov().main(data, 10)
#     return sentence




if __name__ == '__main__':
    app.run(debug=True)
