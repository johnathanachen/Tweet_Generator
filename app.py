from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello():
    return "hello the name is Johno and I love to ing and dance"


if __name__ == '__main__':
    app.run(debug=True)
