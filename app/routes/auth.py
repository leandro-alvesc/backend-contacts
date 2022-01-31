from app.decorators import Decorators as dec
from flask import Blueprint, jsonify
from app.models.users import user_schema
from app.controllers.users import UsersController

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['POST'])
@dec.required_login
def login(token, *args, **kwargs):
    return jsonify({'token': token})


@auth.route('/register', methods=['POST'])
@dec.required_schema(user_schema)
def register(body, *args, **kwargs):
    user = UsersController.insert_user(**body)
    return jsonify(user_schema.dump(user))
