from flask import Flask  # First we imported the flask class


app = Flask(__name__)  # create an instance of this class as "app"


@app.route('/')  # then we use route() decorator to tell flask what to do. Flask url should trigger our function


def hello_form():
    return "<h1><strong>hello is a form</h1>"
    #  the function returns the message on the browser


if __name__ == '__main__':
    app.run(debug=True)
