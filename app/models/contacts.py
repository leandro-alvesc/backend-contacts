from marshmallow import fields, validate

from . import db, ma


class Contacts(db.Model):
    __tablename__ = 'contacts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(60), nullable=False)
    phone = db.Column(db.String(15), nullable=False, unique=True)
    deleted = db.Column(db.Boolean(), default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('Users')

    def __init__(self, name, phone, user_id) -> None:
        self.name = name
        self.phone = phone
        self.user_id = user_id


class ContactsSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(2, 60))
    phone = fields.Str(required=True, validate=validate.Length(8, 15))
    deleted = fields.Bool()
    user_id = fields.Int(dump_only=True)


contact_schema = ContactsSchema()
partial_contact_schema = ContactsSchema(partial=True)
contacts_schema = ContactsSchema(many=True)
