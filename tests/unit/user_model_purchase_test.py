import unittest
from unittest import TestCase
from market.models import User ,Item

class UserModelPurchaseTest(TestCase):

    test_user = User(id=2,
                username="Thabo",
                email_address="thabo@gmail.com",
                password_hash="vink4013",
                budget=7000)

    test_item = Item(id=2,
                name="Aduino-Rasberry-Pi",
                price=2500,
                barcode="******coode****",
                description="Mini computer for micro controller,and personal Iot Project",
                )

    def test_user_purchase(self,item_object):
        """
        this test checks/assert verifies the output
        ..return item of purchase functions,
        if the created user...
         can purchase an  the created item from my tables
        """
        self.assertEqual(self.test_user.budget>=self.test_item.price)

