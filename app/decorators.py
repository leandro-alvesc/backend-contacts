from functools import wraps

from flask import jsonify, request
from flask_marshmallow import Schema
import jwt
import app
from app.auth.services import AuthService
from app.controllers.users import UsersController

from app.exceptions import BadRequest


class Decorators:
    @staticmethod
    def required_schema(schema: Schema):
        def _required_schema(f):
            @wraps(f)
            def __required_schema(*args, **kwargs):
                body = request.json
                if not isinstance(body, dict):
                    raise BadRequest({
                        'code': 'REQUIRED_BODY'
                    })

                errors = schema.validate(body)
                if errors:
                    return jsonify(errors), 400

                return f(body=schema.load(body), *args, **kwargs)
            return __required_schema
        return _required_schema

    @staticmethod
    def required_login(f):
        @wraps(f)
        def _required_login(*args, **kwargs):
            auth = request.authorization

            if not auth or not auth.username or not auth.password:
                raise BadRequest({
                    'code': 'REQUIRED_LOGIN',
                    'message': 'User and Password required'
                })
            token = AuthService.auth(auth.username, auth.password)
            return f(token=token, *args, **kwargs)
        return _required_login

    @staticmethod
    def required_token(f):
        @wraps(f)
        def _required_token(*args, **kwargs):
            bearer_token = request.headers.get('Authorization')

            if not bearer_token:
                raise BadRequest({
                    'code': 'REQUIRED_BEARER_TOKEN',
                    'message': 'Token required'
                })

            token = bearer_token.split()[-1]

            try:
                jwt_info = jwt.decode(token, app.config.JWT_SECRET_KEY,
                                      algorithms=["HS256"])

                username = jwt_info.get('sub')
                user = UsersController.get_user_by_username(username)
                return f(user=user, *args, **kwargs)
            except jwt.ExpiredSignatureError:
                return {'code': 'EXPIRED_TOKEN'}, 401
            except jwt.InvalidTokenError:
                return {'code': 'INVALID_TOKEN'}, 401
        return _required_token
