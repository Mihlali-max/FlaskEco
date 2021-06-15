from unittest import TestCase
from market.models import User, Item
from market import db
from tests.base_test import BaseTest
from market import bcrypt, db

class TestAllModels(BaseTest):
    def test_user_is_created(self):
        new_user = User(id =0,
                        username='Namey',
                        email_address='mail@gmail.com',
                        password_hash='453545zdfds',
                        budget =1000,
        )
        self.assertEqual(new_user.id,0)
        self.assertAlmostEqual(new_user.password_hash,'453545zdfds')
        self.assertEqual(new_user.username, 'Namey')
        self.assertEqual(new_user.email_address, 'mail@gmail.com')
        self.assertEqual(new_user.budget,1000)

    def testing_Items(self):
     new_user = Item(id=0,
                        name='Namey',
                        price=420,
                        barcode='453545zdfds',
                        description='Good',
                        owner =1000
                        )
     self.assertEqual(new_user.id, 0)
     self.assertEqual(new_user.name, 'Namey')
     self.assertAlmostEqual(new_user.price, 420)
     self.assertEqual(new_user.barcode,'453545zdfds')
     self.assertEqual(new_user.description,'Good')
     self.assertEqual(new_user.owner, 1000)

    def test_item_repr_method(self):
        item = Item(name='Phone', price=3000, barcode='jhdjzhcbjsd', description='New')

        new_item = item.__repr__()

        self.assertEqual(new_item, 'Item Phone')


    def test_prettier_budget(self):
        budget_variable = User(username='MihlaliM' , email_address= 'momozamihlali@gmail.com' ,budget =4000)
        self.assertEqual(budget_variable.budget, 4000)


    # def test_sell_Item(self):
    #     Item_Sold = Item(id=1 ,name ='Iphone2',price=2000,barcode='908098',description='latest model',owner='Mihlali')
    #     User_ = User(username='MihlaliM',password_hash='MihlaliM',email_address='momozamihlali@gmail.com',budget=3000).can_sell(Item_Sold)
    #     self.assertFalse(User_)

    def test_item_sell_method(self):
        user = User(id=1, username='Mihlali', email_address='momozamihl@gmail.com', password_hash='Mihlali', budget=2000)
        item = Item(name='Phone', price=2000, barcode='gfhgfhgf', description='new', owner=1)
        can_sell = item.sell(user)
        db.session.commit()
        self.assertIsNone(can_sell)

    def test_item_buy_method(self):
        user = User(id=1, username='Mihlali', email_address='mihlalimom@gmail.com', password_hash='Mihlali', budget=3000)
        item = Item(name='Phone', price=2000, barcode='jhgjhgjh', description='Model', owner=1)
        buy = item.buy(user)
        db.session.commit()
        self.assertIsNone(buy)


    def testing_password(self):
        user = User(username='Namey', email_address='mihlalimom@gmail.com', password_hash='MihlaliM',
                    budget=5000).password_hash

        self.assertEqual(user, 'MihlaliM')

    def testing_password(self):
        password = 'MihlaliM'
        password_hash = bcrypt.generate_password_hash(password)

        self.assertTrue(password_hash, 'MihlaliM')

    def test_password_correction(self):
        password = 'MihlaliM'
        pw_hash = bcrypt.generate_password_hash(password)

        wrong_password = 'hello'
        user = bcrypt.check_password_hash(pw_hash, wrong_password)
        self.assertFalse(user)












