from app.decorators import Decorators as dec
from app.models.users import user_schema
from flask import Blueprint, jsonify

auth = Blueprint('auth', __name__)


@auth.route('/user', methods=['GET'])
@dec.required_token
def get_current_user(user, *args, **kwargs):
    return jsonify(user_schema.dump(user))


@auth.route('/login', methods=['POST'])
@dec.required_login
def login(token, *args, **kwargs):
    return jsonify({'token': token})
