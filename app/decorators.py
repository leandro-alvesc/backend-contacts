from functools import wraps
from flask import jsonify, request
from flask_marshmallow import Schema


class Decorators:
    @staticmethod
    def required_schema(schema: Schema):
        def _required_schema(f):
            @wraps(f)
            def __required_schema(*args, **kwargs):
                body = request.json
                if not isinstance(body, dict):
                    return {'code': 'REQUIRED_BODY'}, 400

                errors = schema.validate(body)
                if errors:
                    return jsonify(errors), 400

                return f(body=schema.load(body), *args, **kwargs)
            return __required_schema
        return _required_schema
