# flake8: noqa
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
ma = Marshmallow()

from .users import Users
from .contacts import Contacts
