from unittest import TestCase
from market.models import User, Item
from market import db
from tests.base_test import BaseTest

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

    def testing_crud(self):
        with self.app_context:
            with self.app:
                new_note = User(id =0,
                        username='Namey',
                        email_address='mail@gmail.com',
                        password_hash='453545zdfds',
                        budget =1000,
        )

                # assert that this item does not exist in the db
                results = db.session.query(User).filter_by(id =0,
                        username='Namey',
                        email_address='mail@gmail.com',
                        password_hash='453545zdfds',
                        budget =1000,
        ).first()
                self.assertIsNone(results)

                # save to db
                User.session.add(new_note)
                User.session.commit()

                # assert that it does exist in db
                results = db.session.query(User).filter_by(id =0,
                        username='Namey',
                        email_address='mail@gmail.com',
                        password_hash='453545zdfds',
                        budget =1000,
        ).first()
                self.assertIsNotNone(results)


                # delete from db
                db.session.delete(new_note)
                db.session.commit()

                 # assert it no longer exists in db
                results = db.session.query(User).filter_by(id =0,
                        username='Namey',
                        email_address='mail@gmail.com',
                        password_hash='453545zdfds',
                        budget =1000,
        ).first()
                self.assertIsNone(results)

    def test_prettier_budget(self):
        budget_variable = User(username='MihlaliM' , email_address= 'momozamihlali@gmail.com' ,budget =4000)
        self.assertEqual(budget_variable.budget, 4000)


    def test_Item_Purchase(self):
        Item_Info=Item(id=1 ,name ='Iphone2',price=2000,barcode='908098',description='latest model',owner='Mihlali')
        purchase=User(username='MihlaliM',password_hash='MihlaliM',email_address='momozamihlali@gmail.com',budget=3000).can_purchase(Item_Info)
        self.assertTrue(purchase)

