import os
import sys

SRC_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
if SRC_PATH not in sys.path:
    sys.path.insert(0, SRC_PATH)

import unittest
from datetime import date, timedelta

from admin import Admin
from pharmacy import Pharmacy
from pharmacist import Pharmacist
from item import Item


class AdminTest(unittest.TestCase):

    def setUp(self):
        self.admin = Admin("Alice", 1, "08011111111")
        self.pharmacy = Pharmacy()
        self.pharmacist = Pharmacist("John", "08022222222")
        self.item = Item(
            "Paracetamol", 500, date.today() + timedelta(days=30), 10
        )

    def test_admin_attributes(self):
        self.assertEqual(self.admin.name, "Alice")
        self.assertEqual(self.admin.id, 1)

    def test_update_admin_id(self):
        self.admin.id = 5
        self.assertEqual(self.admin.id, 5)

    def test_register_pharmacist_assigns_id(self):
        result = self.admin.register_pharmacist(self.pharmacy, self.pharmacist)
        self.assertTrue(result)
        self.assertEqual(self.pharmacist.id, 1)
        self.assertIn(self.pharmacist, self.pharmacy.pharmacists)

    def test_pharmacists_receive_unique_ids(self):
        another = Pharmacist("Mary", "08033333333")
        self.assertTrue(self.admin.register_pharmacist(self.pharmacy, self.pharmacist))
        self.assertTrue(self.admin.register_pharmacist(self.pharmacy, another))
        self.assertEqual(self.pharmacist.id, 1)
        self.assertEqual(another.id, 2)

    def test_duplicate_registration_is_rejected(self):
        self.assertTrue(self.admin.register_pharmacist(self.pharmacy, self.pharmacist))
        self.assertFalse(self.admin.register_pharmacist(self.pharmacy, self.pharmacist))
        self.assertEqual(self.pharmacist.id, 1)
        self.assertEqual(len(self.pharmacy.pharmacists), 1)

    def test_remove_pharmacist(self):
        self.admin.register_pharmacist(self.pharmacy, self.pharmacist)
        result = self.admin.remove_pharmacist(self.pharmacy, self.pharmacist)
        self.assertTrue(result)
        self.assertNotIn(self.pharmacist, self.pharmacy.pharmacists)

    def test_add_stock(self):
        result = self.admin.add_stock(self.pharmacy, self.item)
        self.assertTrue(result)
        self.assertIn(self.item, self.pharmacy.items)

    def test_update_stock(self):
        result = self.admin.update_stock(self.item, 25)
        self.assertTrue(result)
        self.assertEqual(self.item.quantity, 25)

    def test_reject_invalid_stock_quantity(self):
        result = self.admin.update_stock(self.item, 0)
        self.assertFalse(result)
        self.assertEqual(self.item.quantity, 10)

    def test_get_low_stock(self):
        self.item.quantity = 2
        self.pharmacy.add_item(self.item)
        result = self.admin.get_low_stock(self.pharmacy, 5)
        self.assertIn(self.item, result)

    def test_get_expired_stock(self):
        expired_item = Item(
            "Expired Drug", 200, date.today() - timedelta(days=1), 5
        )
        self.pharmacy.add_item(expired_item)
        result = self.admin.get_expired_stock(self.pharmacy)
        self.assertIn(expired_item, result)


if __name__ == "__main__":
    unittest.main()
