#!/usr/bin/env python3
"""Flask app with Babel for internationalization"""

from flask import Flask, request, render_template
from flask_babel import Babel
from os import getenv

# Initialize Flask application
app = Flask(__name__)
babel = Babel(app)


class Config:
    """Configuration class for the Flask app."""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Apply the configuration to the app
app.config.from_object(Config)


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """Render the homepage template."""
    return render_template('3-index.html')


@babel.localeselector
def get_locale() -> str:
    """Select the best language match based on the request."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    # Retrieve host and port from environment variables with defaults
    host = getenv("API_HOST", "0.0.0.0")
    port = int(getenv("API_PORT", "5000"))
    # Run the application
    app.run(host=host, port=port, debug=True)
