from base64 import b64encode
import unittest

from app import app as my_app
from app import db


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.app = my_app
        self.client = self.app.test_client()
        self._ctx = self.app.test_request_context()
        self._ctx.push()

        db.create_all()

        credentials = b64encode(b'unittest:test12345').decode('utf-8')
        self.login = self.client.post(
            '/auth/login', headers={"Authorization": f"Basic {credentials}"})
        self.token = self.login.json.get('token')
        self.user = self.client.get(
            '/auth/user', headers={"Authorization": f"Bearer {self.token}"})

    def test_login(self):
        self.assertEqual(200, self.login.status_code)

    def test_token(self):
        self.assertEqual(200, self.user.status_code)

    def test_content_type(self):
        self.assertIn('application/json', self.user.content_type)
