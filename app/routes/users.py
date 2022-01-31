from flask import Blueprint, jsonify
from app.controllers.users import UserController
from app.decorators import Decorators as dec
from app.models.users import user_schema, users_schema

users = Blueprint('users', __name__)


@users.route('', methods=['GET'])
def get_users(*args, **kwargs):
    users = UserController.get_users()
    return jsonify(users_schema.dump(users))


@users.route('', methods=['POST'])
@dec.required_schema(user_schema)
def insert_user(body, *args, **kwargs):
    user = UserController.insert_user(**body)
    return jsonify(user_schema.dump(user))


@users.route('/<key>', methods=['GET'])
def get_user_by_id(key, *args, **kwargs):
    user = UserController.get_user_by_id(key)
    if not user:
        return {'code': 'NOT_FOUND'}, 404
    return jsonify(user_schema.dump(user))
