from flask import Flask
from sampling import *
from histo_dict import *

app = Flask(__name__)

@app.route("/")
def hello():
    return run_sampling()


if __name__ == '__main__':
    app.run(debug=True)
