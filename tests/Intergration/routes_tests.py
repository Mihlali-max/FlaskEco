from unittest import TestCase
from tests.base_test import BaseTest
from flask import request

from flask import request
from tests.base_test import BaseTest


class TestHomeRoute(BaseTest):
    def test_home(self):
        with self.app:
            with self.app_context:
                    response = self.app.get('/home', follow_redirects=True)

                    self.assertEqual('http://localhost/home', request.url)
                    self.assertIn(b'Start purchasing products by clicking the link below', response.data)
                    self.assertTrue(response.status_code, 200)

    def test_route(self):
        with self.app:
                with self.app_context:
                    response = self.app.get('/', follow_redirects=True)

                    self.assertEqual('http://localhost/', request.url)
                    self.assertIn(b'Start purchasing products by clicking the link below', response.data)

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
    #
    # def test_market_route_(self):
    #     with self.app:
    #         budget_variable = self.app.post(username='MihlaliM', email_address='momozamihlali@gmail.com', budget=4000)
    #         self.assertEqual(budget_variable.budget, 4000)
    #
    # def test_Item_Purchase(self):
    #     Item_Info=Item(id=1 ,name ='Iphone2',price=2000,barcode='908098',description='latest model',owner='Mihlali')
    #     purchase=User(username='MihlaliM',password_hash='MihlaliM',email_address='momozamihlali@gmail.com',budget=3000).can_purchase(Item_Info)
    #     self.assertTrue(purchase)




