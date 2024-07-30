#!/usr/bin/env python3
"""Route module for the API - Force locale with URL parameter"""

from flask import Flask, request, render_template
from flask_babel import Babel
from os import getenv

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
    Return: 4-index.html
    """
    return render_template('4-index.html')

@babel.localeselector
def get_locale() -> str:
    """Determine the best match for supported languages or use URL parameter"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = int(getenv("API_PORT", "5000"))
    app.run(host=host, port=port)