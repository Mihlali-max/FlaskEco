from unittest import TestCase
from market.models import User, Item

class TestAllModels(TestCase):
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
                        price=0,
                        barcode='453545zdfds',
                        description='Good',
                        owner =1000

                        )
     self.assertEqual(new_user.id, 0)
     self.assertEqual(new_user.name, 'Namey')
     self.assertAlmostEqual(new_user.price, 0)
     self.assertEqual(new_user.barcode,'453545zdfds')
     self.assertEqual(new_user.description,'Good')
     self.assertEqual(new_user.owner, 1000)





