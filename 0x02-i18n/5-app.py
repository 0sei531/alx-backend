#!/usr/bin/env python3
"""Route module for the API - Mock logging in"""

from flask import Flask, request, render_template, g
from flask_babel import Babel
from os import getenv
from typing import Union

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app = Flask(__name__)
babel = Babel(app)

class Config(object):
    """Configuration class for Babel"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

# Set the above class object as the configuration for the app
app.config.from_object(Config)

@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """GET /
    Return: 5-index.html
    """
    return render_template('5-index.html')

@babel.localeselector
def get_locale() -> str:
    """Determine the best match for supported languages or use URL parameter"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

def get_user() -> Union[dict, None]:
    """Return user dictionary if ID can be found"""
    user_id = request.args.get('login_as')
    if user_id:
        user = users.get(int(user_id))
        return user
    return None

@app.before_request
def before_request() -> None:
    """Find user and set as global on flask.g.user"""
    g.user = get_user()

if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = int(getenv("API_PORT", "5000"))
    app.run(host=host, port=port)
