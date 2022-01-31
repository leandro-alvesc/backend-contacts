from flask import Blueprint, jsonify
from app.controllers.users import UserController
from app.decorators import Decorators
from app.models.users import user_schema

users = Blueprint('users', __name__)


@users.route('', methods=['GET'])
def get_users():
    return jsonify()


@users.route('', methods=['POST'])
@Decorators.required_schema(user_schema)
def insert_user(body, *args, **kwargs):
    user = UserController.insert_user(**body)
    return jsonify(user_schema.dump(user))
