from cleanup import Clean
from markov import Markov

file_name = "transcript.txt"
data = Clean().clean_text(file_name)
sentence = Markov().main(data, 10)

print(sentence)
