import app
from app.exceptions import InternalServerError
from app.models.contacts import Contacts
from app.models import db


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
    def insert_contact(user, name, phone):
        contact = Contacts(name=name, phone=phone, user_id=user.id)

        try:
            db.session.add(contact)
            db.session.commit()
            return contact
        except Exception as e:
            app.logger.error(str(e))
            message = e.args[0].split(') ')
            message = message[1].split(' "')
            raise InternalServerError({
                'code': 'INTERNAL_SERVER_ERROR',
                'message': message[0]
            })
