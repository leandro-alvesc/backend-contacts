from os import environ

from config import get_env_config, get_logger_config
from flask import Flask
from flask_migrate import Migrate

from app.routes.contacts import contacts
from app.routes.users import users
from app.routes.users import auth

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

# Migrate
migrate = Migrate(app, db)

# Register blueprints
app.register_blueprint(contacts, url_prefix='/contacts')
app.register_blueprint(users, url_prefix='/users')
app.register_blueprint(auth, url_prefix='auth')
