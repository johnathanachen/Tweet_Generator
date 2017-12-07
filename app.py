from flask import Flask, render_template
from cleanup import Clean
from markov import Markov

app = Flask(__name__)

file_name = "transcript.txt"
data = Clean().clean_text(file_name)

@app.route('/', methods=['GET', 'POST'])
def hello():
    sentence = Markov().main(data, 10)
    count = read_current_count()
    new_count = write_new_count()
    return render_template("index.html", sentence=sentence, count=count)

def read_current_count():
    text_file = open("counter.txt", "r")
    count = text_file.read()
    return count

def write_new_count():
    f = open("counter.txt", "r")
    data = f.read()
    new_count = int(data) + 1
    string_format = str(new_count)
    f = open("counter.txt", "w")
    print(string_format)
    f.write(string_format)

@app.route('/new_text', methods=['GET', 'POST'])
def new_text():
    sentence = Markov().main(data, 10)
    return sentence


if __name__ == '__main__':
    app.run(debug=True)
