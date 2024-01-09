#!/usr/bin/env python3
""" 3-app """

from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Dict, Union

app = Flask(__name__)
babel = Babel(app)


class Config:
    """ Config class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(id) -> Union[Dict, None]:
    """ returns a user dict
    """
    return users.get(int(id), None)


@babel.localeselector
def get_locale():
    """ get_locale
    """
    if request.args and request.args.get('locale') in app.config['LANGUAGES']:
        return request.args['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.before_request
def before_request():
    """ executes before request
    """
    id = request.args.get('login_as', 0)
    setattr(g, 'user', get_user(id))


@app.route('/', strict_slashes=False)
def index():
    """ index route
    """
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run()
