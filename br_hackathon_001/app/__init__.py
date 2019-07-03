# app/__init__.py

from flask import Flask

# Initialize the app
app = Flask(__name__, instance_relative_config=True)

# Load the routes
from app import routes
from app.utils import strings
from app.utils import json

# from app.auth import bp as auth_bp


# Load the config file
app.config.from_object('config')

if __name__ == '__app__':
    app.run()