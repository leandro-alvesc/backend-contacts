from os import environ

from flask_sqlalchemy import SQLAlchemy

from config import get_env_config, get_logger_config
from flask import Flask

from app.views.contacts import contacts

# ENV Config
ENV = environ.get('ENV', 'LOCAL')
config = get_env_config(ENV)

# Logger config
logger = get_logger_config()

# App config
app = Flask(__name__)

app.config.from_object(config)

# DB Config
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Register blueprints
app.register_blueprint(contacts, url_prefix='/contacts')
