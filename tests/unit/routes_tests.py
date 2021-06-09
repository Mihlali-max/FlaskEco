from unittest import TestCase
from tests.base_test import BaseTest
from tests.base_test import BaseTest
from flask import request
from market import db
from flask_login import current_user ,AnonymousUserMixin

class Testing_routes(TestCase):

    def test_home_route(self):
        with self.app:
            response = self.app.get('/home', follow_redirects=True)
            self.assertEqual(response.status_code, 200)

    def test_market_route(self):
        with self.app:
            response = self.app.get('/market', follow_redirects=True)
            self.assertEqual(response.status_code, 200)

    def test_register_route(self):
        with self.app:
            response = self.app.get('/register', follow_redirects=True)
            self.assertEqual(response.status_code, 200)



    def test_login_route(self):
        with self.app:
            response = self.app.get('/login', follow_redirects=True)
            self.assertEqual(response.status_code, 200)