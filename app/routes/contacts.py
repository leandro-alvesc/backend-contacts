from flask import Blueprint, jsonify
from app.controllers.contacts import ConctactsController
from app.decorators import Decorators as dec
from app.models.contacts import contact_schema, contacts_schema

contacts = Blueprint('contacts', __name__)


@contacts.route('', methods=['GET'])
@dec.required_token
def get_contacts(user, *args, **kwargs):
    contacts = ConctactsController.get_contacts(user)
    return jsonify(contacts_schema.dump(contacts))


@contacts.route('', methods=['POST'])
@dec.required_token
@dec.required_schema(contact_schema)
def insert_contact(user, body, *args, **kwargs):
    contact = ConctactsController.insert_contact(user, **body)
    return jsonify(contact_schema.dump(contact))


@contacts.route('/<key>', methods=['DELETE'])
@dec.required_token
def delete_contact(key, *args, **kwargs):
    ConctactsController.delete_contact(key)
    return jsonify(), 204
