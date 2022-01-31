from datetime import datetime, timedelta
from app.controllers.users import UsersController
import jwt
import app


class AuthService:
    @classmethod
    def auth(cls, username, password):
        user = UsersController.check_auth(username, password)
        jwt = cls._generate_jwt(user.username)
        return jwt

    @staticmethod
    def _generate_jwt(username):
        return jwt.encode({
            'sub': username,
            'iat': datetime.utcnow(),
            'exp': datetime.utcnow() + timedelta(minutes=3600 * 31)
        }, app.config.JWT_SECRET_KEY, algorithm='HS256')
