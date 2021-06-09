from tests.base_test import BaseTest
from flask import request
from market import db
from market.models import User, Item
from flask_login import current_user ,AnonymousUserMixin

class TestRegister(BaseTest):

    # test signing up user successfully
    def test_sign_up_post_success(self):
        with self.app:
            # create a post req with valid data
            response = self.app.post('/register',
                                    data=dict(username='Namey', email_address = 'mail@gmail.com', password1='453545zdfds',password2='453545zdfds'),
                                    follow_redirects=True)
            # assert that new user is created in db
            user = db.session.query(User).filter_by(username='Namey').first()
            self.assertTrue(user)
            # assert that flash message is shown
            self.assertIn(b'Account created successfully! You are now logged in as ', response.data)
            print(response.data)
            # assert that user is logged in'
            self.assertEqual(current_user.get_id(), '1')
            # assert that page is redirected

    def test_Login(self):
        with self.app:
            response = self.app.post('/register',
                                     data=dict(username='Namey', email_address='mail@gmail.com',
                                               password1='453545zdfds', password2='453545zdfds'),
                                     follow_redirects=True)
            # assert that new user is created in db
            user = db.session.query(User).filter_by(username='Namey').first()
            self.assertTrue(user)
            # assert that flash message is shown
            self.assertIn(b'Account created successfully! You are now logged in as ', response.data)
            # assert that user is logged in
            self.assertEqual(current_user.get_id(), '1')
            # assert that page is redirected
            resp = self.app.post('/login', data =dict(username='Namey', password='453545zdfds'),follow_redirects=True)

            self.assertIn(b'Success! You are logged in as:',resp.data)

            respa = self.app.get('/logout', follow_redirects=True)
            self.assertIn(b'You have been logged out!',respa.data)
            self.assertEqual(respa.status_code, 200)
