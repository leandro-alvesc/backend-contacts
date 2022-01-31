from . import db, ma


class Contacts(db.Model):
    __tablename__ = 'contacts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(60), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    deleted = db.Column(db.Boolean())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('Users')

    def __init__(self, name, phone) -> None:
        self.name = name
        self.phone = phone


class ContactsSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'phone', 'deleted')


contact_schema = ContactsSchema()
contacts_schema = ContactsSchema(many=True)
