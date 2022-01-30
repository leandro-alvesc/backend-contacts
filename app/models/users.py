from datetime import datetime

from . import db, ma


class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(15))
    created_on = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, username, password, name, email, phone) -> None:
        self.username = username
        self.password = password
        self.name = name
        self.email = email
        self.phone = phone

    def __repr__(self) -> str:
        return f'<id {self.id}>'


class UsersSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'password', 'name', 'email', 'phone',
                  'created_on')


user_schema = UsersSchema()
users_schema = UsersSchema(many=True)
