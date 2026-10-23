
import unittest
from datetime import date, timedelta

from admin import Admin
from pharmacist import Pharmacist
from item import Item
from pharmacy import Pharmacy


class PharmacistTest(unittest.TestCase):

    def setUp(self):
        self.pharmacist = Pharmacist("John", "08012345678")
        self.pharmacy = Pharmacy()
        self.item = Item(
            "Paracetamol", 500, date.today() + timedelta(days=30), 10
        )
        self.pharmacy.add_item(self.item)
        # Existing sale tests model a pharmacist who has been registered.
        self.pharmacist.id = 10

    def test_pharmacist_id(self):

        self.assertEqual(self.pharmacist.id, 10)

    def test_search_item(self):

        self.assertIs(self.pharmacist.search_item(self.pharmacy, "Paracetamol"), self.item)

    def test_check_availability(self):

        self.assertTrue(self.pharmacist.check_availability(self.item, 5))

    def test_sell_item(self):
        result = self.pharmacist.sell_item(self.item, 3)
        self.assertEqual(result, 1500)
        self.assertEqual(self.item.quantity, 7)

    def test_pharmacist_without_id_cannot_sell(self):
        self.pharmacist.id = None
        result = self.pharmacist.sell_item(self.item, 3)

        self.assertIsNone(result)
        self.assertEqual(self.item.quantity, 10)

    def test_admin_registration_assigns_id_before_sale(self):
        unregistered = Pharmacist("Mary", "08099999999")
        admin = Admin("Alice", 1, "08011111111")

        self.assertIsNone(unregistered.id)
        self.assertTrue(admin.register_pharmacist(self.pharmacy, unregistered))
        self.assertIsNotNone(unregistered.id)
        result = unregistered.sell_item(self.item, 2)
        self.assertEqual(result, 1000)
        self.assertEqual(self.item.quantity, 8)

    def test_sale_fails_when_stock_is_insufficient(self):
        result = self.pharmacist.sell_item(self.item, 15)
        self.assertIsNone(result)
        self.assertEqual(self.item.quantity, 10)

    def test_sale_fails_for_expired_item(self):
        expired_item = Item(
            "Expired Drug", 200, date.today() - timedelta(days=1), 5
        )
        result = self.pharmacist.sell_item(expired_item, 2)
        self.assertIsNone(result)
        self.assertEqual(expired_item.quantity, 5)

    def test_sale_fails_for_invalid_quantity(self):
        result = self.pharmacist.sell_item(self.item, 0)
        self.assertIsNone(result)
        self.assertEqual(self.item.quantity, 10)


if __name__ == "__main__":
    unittest.main()
