#!/usr/bin/env python3
""" Flask application with Babel setup """

from flask import Flask, render_template
from flask_babel import Babel
from os import getenv

# Application and Babel setup
app = Flask(__name__)
babel = Babel(app)


class Config:
    """Configuration settings for the Flask app."""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Determine the best language match based on request."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """Render the homepage template."""
    return render_template('1-index.html')


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = int(getenv("API_PORT", "5000"))
    app.run(host=host, port=port, debug=True)
