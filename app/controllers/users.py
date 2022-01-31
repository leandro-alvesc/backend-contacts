from werkzeug.security import generate_password_hash
from app.models import db
from app.models.users import Users
from app.exceptions import InternalServerError


class UserController:
    @staticmethod
    def get_users():
        pass

    @staticmethod
    def get_user_by_id():
        pass

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
