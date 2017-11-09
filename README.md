<h1 align="center">
<img width="200px" src="https://upload.wikimedia.org/wikipedia/en/thumb/4/47/Twitter_2010_logo_-_from_Commons.svg/1024px-Twitter_2010_logo_-_from_Commons.svg.png">
<br>
Tweet Generator
</h1>

### Key Features of the Application
The Key features of this application is the ability to generate random words from a collection of speech transcripts and develop a sentence by implementing the Markov chain.

### Understanding File Functions and Variable Names
Listed below in 'Architecture' is a description of each file and every variable should have pretty clear naming to be easily readable and understandable. 

- What are the scopes of variables and are they appropriate for their use case? If there are global variables, why are they needed?
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
