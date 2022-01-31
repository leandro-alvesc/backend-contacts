import re

import app
from app.exceptions import BadRequest, Forbidden, InternalServerError
from app.models import db
from app.models.users import Users
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.security import check_password_hash, generate_password_hash


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

    @classmethod
    def insert_user(cls, username, password, name, email, phone=''):
        password = generate_password_hash(password)
        user = Users(
            username=username,
            password=password,
            name=name,
            email=email,
            phone=phone
        )

        db.session.add(user)
        cls._commit_session()
        return user

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
