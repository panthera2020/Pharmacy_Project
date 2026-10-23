import os
import sys

SRC_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
if SRC_PATH not in sys.path:
    sys.path.insert(0, SRC_PATH)

import unittest
from datetime import date, timedelta

from customer import Customer
from item import Item
from pharmacy import Pharmacy


class CustomerTest(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Peter", "08012345678")
        self.pharmacy = Pharmacy()
        self.item = Item(
            "Paracetamol", 500, date.today() + timedelta(days=30), 10
        )
        self.pharmacy.add_item(self.item)

    def test_customer_attributes(self):
        self.assertEqual(self.customer.name, "Peter")
        self.assertEqual(self.customer.phone_number, "08012345678")

    def test_customer_id(self):
        self.customer.id = 20
        self.assertEqual(self.customer.id, 20)

    def test_search_item(self):
        self.assertIs(self.customer.search_item(self.pharmacy, "Paracetamol"), self.item)

    def test_add_to_cart(self):
        self.assertTrue(self.customer.add_to_cart(self.item, 2))
        self.assertEqual(self.customer._cart[self.item], 2)
        self.assertEqual(self.item.quantity, 10)

    def test_add_same_item_twice(self):
        self.customer.add_to_cart(self.item, 2)
        self.customer.add_to_cart(self.item, 3)
        self.assertEqual(self.customer._cart[self.item], 5)

    def test_reject_invalid_cart_quantity(self):
        self.assertFalse(self.customer.add_to_cart(self.item, 0))
        self.assertEqual(self.customer._cart, {})

    def test_remove_from_cart(self):
        self.customer.add_to_cart(self.item, 2)
        self.assertTrue(self.customer.remove_from_cart(self.item))
        self.assertEqual(self.customer._cart, {})

    def test_update_cart_quantity(self):
        self.customer.add_to_cart(self.item, 2)
        self.assertTrue(self.customer.update_cart_quantity(self.item, 5))
        self.assertEqual(self.customer._cart[self.item], 5)

    def test_cart_total(self):
        self.customer.add_to_cart(self.item, 3)
        self.assertEqual(self.customer.get_cart_total(), 1500)

    def test_successful_purchase(self):
        self.customer.add_to_cart(self.item, 3)
        self.assertTrue(self.customer.purchase())
        self.assertEqual(self.item.quantity, 7)
        self.assertEqual(self.customer._cart, {})

    def test_failed_purchase_does_not_reduce_stock(self):
        second_item = Item(
            "Ibuprofen", 700, date.today() + timedelta(days=30), 2
        )
        self.customer.add_to_cart(self.item, 3)
        self.customer.add_to_cart(second_item, 5)
        self.assertFalse(self.customer.purchase())
        self.assertEqual(self.item.quantity, 10)
        self.assertEqual(second_item.quantity, 2)

    def test_customers_have_separate_carts(self):
        another_customer = Customer("Mary", "08099999999")
        self.customer.add_to_cart(self.item, 3)
        self.assertEqual(another_customer._cart, {})


if __name__ == "__main__":
    unittest.main()
