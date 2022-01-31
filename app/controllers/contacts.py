import app
from app.exceptions import InternalServerError, BadRequest
from app.models.contacts import Contacts
from app.models import db
from sqlalchemy.exc import SQLAlchemyError
import re


class ConctactsController:
    @staticmethod
    def get_contacts(user):
        try:
            contacts = Contacts.query.filter(Contacts.user_id == user.id)
            return contacts
        except Exception as e:
            app.logger.error(str(e))
            message = e.args[0].split(') ')
            message = message[1].split(' "')
            raise InternalServerError({
                'code': 'INTERNAL_SERVER_ERROR',
                'message': message[0]
            })

    @staticmethod
    def get_contact_by_id(id):
        contact = Contacts.query.get(id)
        return contact

    @staticmethod
    def get_contact_by_phone(phone):
        try:
            contacts = Contacts.query.filter(Contacts.phone == phone).one()
            return contacts
        except Exception as e:
            app.logger.error(str(e))
            return None

    @classmethod
    def insert_contact(cls, user, name, phone):
        contact = cls.get_contact_by_phone(phone)
        if contact:
            if contact.deleted:
                contact.deleted = False
            else:
                raise BadRequest({
                    'code': 'ALREADY_EXISTS',
                    'message': 'Already exists a contact with this number'
                })
        else:
            contact = Contacts(name=name, phone=phone, user_id=user.id)
            db.session.add(contact)

        cls._commit_session()
        return contact

    @classmethod
    def update_contact(cls, contact_id, **fields):
        contact = cls.get_contact_by_id(contact_id)
        if not contact:
            raise BadRequest({
                'code': 'NOT_FOUND',
                'message': 'Contact not found'
            })

        [setattr(contact, field, fields[field]) for field in fields if hasattr(
            contact, field)]

        cls._commit_session()
        return contact

    @classmethod
    def delete_contact(cls, contact_id):
        contact = cls.get_contact_by_id(contact_id)
        if not contact:
            raise BadRequest({
                'code': 'NOT_FOUND',
                'message': 'Contact not found'
            })
        contact.deleted = True

        cls._commit_session()
        return contact

    @classmethod
    def _commit_session(cls):
        try:
            db.session.commit()
        except SQLAlchemyError as e:
            app.logger.error(str(e))

            raise InternalServerError(cls._format_error_message(e))

    @staticmethod
    def _format_error_message(err):
        message = str(err.__dict__['orig'])
        error_name = type(err.__dict__['orig']).__name__
        code = re.sub('([A-Z][a-z]+)', r' \1',
                      re.sub('([A-Z]+)', r' \1', error_name)).split()
        code = '_'.join(code)
        return {
            'code': code.upper(),
            'message': message
        }
