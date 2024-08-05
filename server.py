from flask import Flask
import random

app = Flask(__name__)


if __name__ == "__main__":
    app.run(debug=True)