import os
from random import randint

from dotenv import find_dotenv, load_dotenv
from flask import Flask

#loading env variables
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
FLASK_APP = os.getenv("FLASK_APP")

# ---------create flask app
app = Flask(__name__)

# ---------gen random number
random_number = randint(1, 9)


# ---------homepage
@app.route('/')
def hello_world():
    return "<h1>Guess a number between 0 and 9!</h1>"\
            "<p>then enter '/yournumber' at the end of the url and press enter!</p>"\
            f"{random_number}<br><img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


# ---------guessed number page
@app.route("/<int:number>")
def guesspage(number):
    if number > random_number:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"
    elif number < random_number:
        return "<h1 style='color: red'>Too low, try again!</h1>"\
            "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"


# ---------run server when you run this script
if __name__ == "__main__":
    app.run(debug=True)