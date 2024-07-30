#!/usr/bin/env python3
"""Route module for the API - Infer appropriate time zone"""

from flask import Flask, request, render_template, g
from flask_babel import Babel
from os import getenv
from pytz import timezone as tz
import pytz.exceptions
from typing import Union, Optional

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Babel configuration"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Set the above class object as the configuration for the app
app.config.from_object(Config)


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """Handle GET / request
    Return: 6-index.html
    """
    return render_template('6-index.html')


@babel.localeselector
def get_locale() -> Optional[str]:
    """Determine the best match for supported languages"""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user() -> Union[dict, None]:
    """Return user dict if ID can be found"""
    user_id = request.args.get('login_as')
    if user_id:
        try:
            user_id = int(user_id)
            return users.get(user_id)
        except ValueError:
            return None
    return None


@app.before_request
def before_request() -> None:
    """Find user and set as global on flask.g.user"""
    g.user = get_user()


@babel.timezoneselector
def get_timezone() -> Optional[str]:
    """Determine the best match for supported timezones"""
    timezone = request.args.get('timezone')
    if timezone:
        try:
            return tz(timezone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            return None
    if g.user and g.user.get('timezone'):
        try:
            return tz(g.user.get('timezone')).zone
        except pytz.exceptions.UnknownTimeZoneError:
            return None
    return app.config['BABEL_DEFAULT_TIMEZONE']


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = int(getenv("API_PORT", "5000"))
    app.run(host=host, port=port)
