from flask import Flask
import random

random_number = random.randint(0, 9)
print(random_number)

app = Flask(__name__)


@app.route("/")
def home():
    return '<h1>Guess the number between 1 to 10</h1> ' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=300px>'


@app.route("/<int:guess>")
def guess_number(guess):
    if guess < random_number:
        return '<h1 style: color=red>Too low, Try again!</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width=300px>'

    elif guess > random_number:
        return '<h1 style: color=red>Too high, Try again!</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width=300px>'

    else:
        return '<h1 style: color=green>"You have guessed right!</h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width=300px>'


if __name__ == "__main__":
    app.run(debug=True)
