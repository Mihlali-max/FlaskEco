
from wtforms.validators import ValidationError
from tests.base_test import BaseTest
from market import db
from market.models import User
from market.forms import RegisterForm


class TestForms(BaseTest):
    def test_username_already_exist(self):
        with self.app:
            with self.app_context:
                response1 = self.app.post('/register',
                                          data=dict(username="MihlaliM", email_address="momozamihla@gmail.com",
                                                    password1="alumna77", password2="alumna77",), follow_redirects=True)

                user = db.session.query(User).filter_by(email_address="momozamihla@gmail.com").first()
                self.assertTrue(user)

                # response = self.app.post('/register',
                #                          data=dict(username="JoeDoe", email_address="joe@gmail.com",
                #                                    password1="202177", password2="202177",), follow_redirects=True)

                class Username():
                    data = "MihlaliM"

                with self.assertRaises(ValidationError) as context:
                    RegisterForm().validate_username(Username)
                    self.assertEqual('Username already exists! Please try a different username', str(context.exception))

    def test_email_already_exists(self):
        with self.app:
            with self.app_context:
                response1 = self.app.post('/register',
                                          data=dict(username="Mihlali", email_address="momozamihla@gmail.com",
                                                    password1="alumna77", password2="alumna77" ,), follow_redirects=True)

                user = db.session.query(User).filter_by(email_address="momozamihla@gmail.com").first()
                self.assertTrue(user)

                class Email:
                    data = "momozamihla@gmail.com"

                with self.assertRaises(ValidationError) as context:
                    RegisterForm().validate_email_address(Email)
                    self.assertEqual('Email Address already exists! Please try a different email address', str(context.exception))