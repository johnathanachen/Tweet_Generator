from flask import Flask
from sampling import *
from histo_dict import *

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello"


if __name__ == '__main__':
    app.run(debug=True)
