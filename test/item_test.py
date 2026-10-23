

import unittest
from datetime import date, timedelta

from item import Item


class ItemTest(unittest.TestCase):

    def setUp(self):
        self.item = Item(
            "Paracetamol", 500, date.today() + timedelta(days=30), 10
        )

    def test_item_attributes(self):
        self.assertEqual(self.item.name, "Paracetamol")
        self.assertEqual(self.item.price, 500)
        self.assertEqual(self.item.quantity, 10)

    def test_update_item_attributes(self):
        self.item.name = "Ibuprofen"
        self.item.price = 700
        self.item.quantity = 20
        self.assertEqual(self.item.name, "Ibuprofen")
        self.assertEqual(self.item.price, 700)
        self.assertEqual(self.item.quantity, 20)

    def test_item_is_available(self):
        self.assertTrue(self.item.is_available(5))

    def test_insufficient_stock_is_not_available(self):
        self.assertFalse(self.item.is_available(11))

    def test_zero_quantity_is_not_available(self):
        self.assertFalse(self.item.is_available(0))

    def test_reduce_stock(self):
        self.assertTrue(self.item.reduce_stock(3))
        self.assertEqual(self.item.quantity, 7)

    def test_cannot_reduce_more_than_available(self):
        self.assertFalse(self.item.reduce_stock(15))
        self.assertEqual(self.item.quantity, 10)

    def test_increase_stock(self):
        self.assertTrue(self.item.increase_stock(5))
        self.assertEqual(self.item.quantity, 15)

    def test_cannot_increase_by_zero(self):
        self.assertFalse(self.item.increase_stock(0))
        self.assertEqual(self.item.quantity, 10)

    def test_expired_item(self):
        expired_item = Item("Old Drug", 200, date.today() - timedelta(days=1), 5)
        self.assertTrue(expired_item.is_expired())

    def test_unexpired_item(self):
        self.assertFalse(self.item.is_expired())


if __name__ == "__main__":
    unittest.main()
