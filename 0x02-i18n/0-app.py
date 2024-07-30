#!/usr/bin/env python3
""" Route module for the API - Basic Flask app """

from flask import Flask, request, render_template
from os import getenv


class Config:
    """Configuration class for Flask app"""
    API_HOST = getenv("API_HOST", "0.0.0.0")
    API_PORT = getenv("API_PORT", 5000)


app = Flask(__name__, static_url_path='')
app.config.from_object(Config)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """ GET /
        Return: 0-index.html
    """
    return render_template('0-index.html')

if __name__ == "__main__":
    app.run(host=app.config['API_HOST'], port=app.config['API_PORT'])
