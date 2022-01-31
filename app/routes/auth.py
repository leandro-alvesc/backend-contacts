from app.decorators import Decorators as dec
from flask import Blueprint, jsonify

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['POST'])
@dec.required_login
def login(token, *args, **kwargs):
    return jsonify({'token': token})
