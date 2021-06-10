from unittest import TestCase
from tests.base_test import BaseTest
from flask import request

class Testing_routes(BaseTest):

    def test_home_route(self):
        with self.app:
            with self.app_context:
                response = self.app.get('/home', follow_redirects=True)
                self.assertEqual('http://localhost/home',request.url)
                self.assertEqual(response.status_code, 200)

    def test_market_route_get(self):
        with self.app:
            response = self.app.get('/market', follow_redirects=True)
            self.assertEqual('http://localhost/login?next=%2Fmarket', request.url)
            self.assertEqual(response.status_code, 200)

    def test_register_route(self):
        with self.app:
            response = self.app.get('/register', follow_redirects=True)
            self.assertEqual('http://localhost/register', request.url)
            self.assertEqual(response.status_code, 200)

    def test_login_route(self):
        with self.app:
            with self.app_context:
                response = self.app.get('/login', follow_redirects=True)
                self.assertEqual('http://localhost/login', request.url)
                self.assertEqual(response.status_code, 200)