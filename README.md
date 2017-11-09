<h1 align="center">
<img width="200px" src="https://2.bp.blogspot.com/-m2spxn5LIJg/VyJNSuwSK2I/AAAAAAAAGhk/htKFLq8eUbIc18atFbPfCINn8l_96rkmwCLcB/s1600/trumpFree_01.png"><br>
<img width="200px" src="https://upload.wikimedia.org/wikipedia/en/thumb/4/47/Twitter_2010_logo_-_from_Commons.svg/1024px-Twitter_2010_logo_-_from_Commons.svg.png">
<br>
</h1>

### Description
This is a random tweet generator that generate short tweets using the Markov chain method and all of Trump's speech transcripts.

## Q&A
<b>What are the key features of the application? Are these clearly separated into their own files, classes, and/or modules?</b>
<br>
<br>
This application has the ability to generate random strings of words from a collection of speech transcripts scraped from the web by implmenting the Markov chain method.

<b>Are the names of files, modules, functions, and variables appropriate and accurate? Would a new programmer be able to understand the names without too much contextual knowledge?</b>
<br>
<br>
Listed below in 'Architecture' is a description of each file and every variable should have pretty clear naming to be easily readable and understandable. 

<b>What are the scopes of variables and are they appropriate for their use case? If there are global variables, why are they needed?</b>
<br>
<br>
There is no global variables, each variable is within the scope of the class or function it resides in.

<b>Are the functions small and clearly specified, with as few side effects as possible?</b>
<br>
<br>
Each function handles one action and is clearly specified with naming conventions and comment descriptions. There is minimal to no side effects.

<b>Are there functions that could be better organized in an Object-Oriented Programming style by defining them as methods of a class?</b>
<br>
<br>
The file Architecture is organized in OOP style

<b>Can files be used as both modules and as scripts?</b>
<br>
<br>

<b>Do modules all depend on each other or can they be used independently?</b>
<br>
<br>


## Architecture
```python
app.py          # main script, uses other modules to generate sentences
cleanup.py      # module for cleaning up source text
tokenize.py     # module for creating lists of tokens from a text
word_count.py   # module for generating histograms from a list of tokens
sample.py       # module for generating a sample word from a histogram
sentence.py     # module for generating a sentence from a histogram
```
