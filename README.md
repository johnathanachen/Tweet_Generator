<h1 align="center">
<img width="200px" src="https://upload.wikimedia.org/wikipedia/en/thumb/4/47/Twitter_2010_logo_-_from_Commons.svg/1024px-Twitter_2010_logo_-_from_Commons.svg.png">
<br>
Tweet Generator
</h1>

## Q&A

<b>What are the key features of the application? Are these clearly separated into their own files, classes, and/or modules?</b>
<br>
This application has the ability to generate random strings of words from a collection of speech transcripts scarped from the web by implmenting the Markov chain method.

### Understanding File Functions and Variable Names
Listed below in 'Architecture' is a description of each file and every variable should have pretty clear naming to be easily readable and understandable. 

### Scopes of Variables
There is no global variables, each variable is within the scope of the class or function it resides in.

### Functions and Side Effects
- Are the functions small and clearly specified, with as few side effects as possible?
- Are there functions that could be better organized in an Object-Oriented Programming style by defining them as methods of a class?
- Can files be used as both modules and as scripts?
- Do modules all depend on each other or can they be used independently?


## Architecture
```python
app.py          # main script, uses other modules to generate sentences
cleanup.py      # module for cleaning up source text
tokenize.py     # module for creating lists of tokens from a text
word_count.py   # module for generating histograms from a list of tokens
sample.py       # module for generating a sample word from a histogram
sentence.py     # module for generating a sentence from a histogram
```
