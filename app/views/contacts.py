from flask import Blueprint, jsonify

contacts = Blueprint('contacts', __name__)


@contacts.route('', methods=['GET'])
def get_contacts():
    return jsonify()
