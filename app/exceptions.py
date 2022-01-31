from werkzeug.exceptions import BadRequest, Forbidden, InternalServerError
from flask import make_response


class BadRequest(BadRequest):
    def __init__(self, response: dict = None):
        super().__init__(response=make_response(response, 400))


class Forbidden(Forbidden):
    def __init__(self, response: dict = None):
        super().__init__(response=make_response(response, 403))


class InternalServerError(InternalServerError):
    def __init__(self, response: dict = None):
        super().__init__(response=make_response(response, 500))
