from flask import Blueprint, jsonify
from app.controllers.contacts import ConctactsController
from app.decorators import Decorators as dec
from app.models.contacts import contacts_schema

contacts = Blueprint('contacts', __name__)


@contacts.route('', methods=['GET'])
@dec.required_token
def get_contacts(user, *args, **kwargs):
    contacts = ConctactsController.get_contacts(user)
    return jsonify(contacts_schema.dump(contacts))
