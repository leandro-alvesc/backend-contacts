from os import environ

from config import get_env_config, get_logger_config
from flask import Flask

from app.routes.contacts import contacts

from .models import db, ma

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
db.init_app(app)
ma.init_app(app)

# Register blueprints
app.register_blueprint(contacts, url_prefix='/contacts')
