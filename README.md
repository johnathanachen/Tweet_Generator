<h1 align="center">
<img width="200px" src="https://2.bp.blogspot.com/-m2spxn5LIJg/VyJNSuwSK2I/AAAAAAAAGhk/htKFLq8eUbIc18atFbPfCINn8l_96rkmwCLcB/s1600/trumpFree_01.png"><br>
<img width="200px" src="https://upload.wikimedia.org/wikipedia/en/thumb/4/47/Twitter_2010_logo_-_from_Commons.svg/1024px-Twitter_2010_logo_-_from_Commons.svg.png">
<br>
</h1>

### Description
This is a random tweet generator that generates short tweets using the Markov chain method from all of Trump's speech transcripts.

# Python Tweet Generator

> Python Tweet Generator is a light weight Markov Model implemented into python


## Installation

Installation is super friendly using `pip`

```
$ pip install -r requirements.txt
$ python3 app.py
```

### Deployment
Install the Heroku toolbelt.
```
heroku create myapp
git push heroku master
```

## Usage
Avaliable online at https://tweetgendonald.herokuapp.com/

## Example

**What are the key features of the application? Are these clearly separated into their own files, classes, and/or modules?**

    -`app.py` - main script for my Flask Server, it uses other modules to generate sentences
    -`cleanup.py` - module for cleaning up source text and generates corpus.txt
    - `histogram.py` - grabs a list of words from a body of text
    - `dictogram.py` - refactoring histogram class to Dictogram class which helps to generates the random_weighted_words
    - `sample.py` - handles all the percentage handling and creating a list of words+occurrences and makes a text file for it.
    - `markov.py` - Markov model module generating tweet sentence word from generate_markov_model

- In Progress Code
    - `crawler.py` # module for creating lists of tokens from a text
    - `markov.py` # Markov model module generating a sentence word from 81490 Shakespeare corpus
    - `twitter.py` # calling the Twitter API  
