import app
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import db
from app.models.users import Users
from app.exceptions import InternalServerError, BadRequest, Forbidden


class UsersController:
    @staticmethod
    def get_users():
        users = Users.query.all()
        return users

    @staticmethod
    def get_user_by_id(id):
        user = Users.query.get(id)
        return user

    @staticmethod
    def get_user_by_username(username):
        try:
            user = Users.query.filter(Users.username == username).one()
            return user
        except Exception as e:
            app.logger.error(str(e))
            raise BadRequest({
                'code': 'NOT_FOUND',
                'message': 'User not found'
            })

    @classmethod
    def check_auth(cls, username, password):
        user = cls.get_user_by_username(username)
        match = check_password_hash(user.password, password)
        if not match:
            raise Forbidden({
                'code': 'INVALID_USER_OR_PASSWORD',
                'message': 'Invalid user or password'
            })
        return user

    @staticmethod
    def insert_user(username, password, name, email, phone=''):
        password = generate_password_hash(password)
        user = Users(
            username=username,
            password=password,
            name=name,
            email=email,
            phone=phone
        )

        try:
            db.session.add(user)
            db.session.commit()
            return user
        except Exception as e:
            message = e.args[0].split(') ')
            message = message[1].split(' "')
            raise InternalServerError({
                'code': 'INTERNAL_SERVER_ERROR',
                'message': message[0]
            })
