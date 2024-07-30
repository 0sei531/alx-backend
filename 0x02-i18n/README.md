# i18n in Flask

This project demonstrates how to implement internationalization (i18n) in a Flask application using Flask-Babel. The app supports multiple languages and dynamically adjusts to the user's locale.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Project Structure](#project-structure)
- [Tasks](#tasks)
  - [Task 0: Basic Flask app](#task-0-basic-flask-app)
  - [Task 1: Basic Babel setup](#task-1-basic-babel-setup)
  - [Task 2: Get locale from request](#task-2-get-locale-from-request)
  - [Task 3: Parametrize templates](#task-3-parametrize-templates)
  - [Task 4: Force locale with URL parameter](#task-4-force-locale-with-url-parameter)
  - [Task 5: Mock logging in](#task-5-mock-logging-in)
  - [Task 6: Use user locale](#task-6-use-user-locale)
  - [Task 7: Infer appropriate time zone](#task-7-infer-appropriate-time-zone)
  - [Task 8: Display the current time](#task-8-display-the-current-time)
- [Contributing](#contributing)
- [License](#license)

## Requirements

- Python 3.7
- Flask 1.1.2
- Flask-Babel 2.0.0
- Ubuntu 18.04 LTS

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/alx-backend.git
    cd alx-backend/0x02-i18n
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:
    ```bash
    python3 app.py
    ```

2. Open your web browser and navigate to `http://localhost:5000`.

## Features

- Basic Flask application setup
- Internationalization with Flask-Babel
- Locale determination from request headers
- Template parametrization for different languages
- Locale override via URL parameters
- Mock user login with specific locales and time zones
- Automatic time zone inference and display

## Project Structure

```plaintext
.
├── app.py
├── babel.cfg
├── requirements.txt
├── templates
│   ├── 0-index.html
│   ├── 1-index.html
│   ├── 3-index.html
│   ├── 4-index.html
│   ├── 5-index.html
│   ├── 6-index.html
│   └── index.html
└── translations
    ├── en
    │   └── LC_MESSAGES
    │       ├── messages.mo
    │       └── messages.po
    └── fr
        └── LC_MESSAGES
            ├── messages.mo
            └── messages.po
