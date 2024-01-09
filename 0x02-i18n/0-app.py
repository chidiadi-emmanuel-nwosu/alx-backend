#!/usr/bin/env python3
""" 0-app """

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ index route
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
