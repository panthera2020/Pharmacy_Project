
import unittest
from datetime import date, timedelta

from pharmacist import Pharmacist
from item import Item
from pharmacy import Pharmacy


class PharmacistTest(unittest.TestCase):

    def setUp(self):
        self.pharmacist = Pharmacist("John", "08012345678")
        self.pharmacy = Pharmacy()

        self.item = Item(
            "Paracetamol",
            500,
            date.today() + timedelta(days=30),
            10
        )

        self.pharmacy.add_item(self.item)

    def test_pharmacist_id(self):
        self.pharmacist.id = 10

        self.assertEqual(self.pharmacist.id, 10)

    def test_search_item(self):
        result = self.pharmacist.search_item(
            self.pharmacy, "Paracetamol"
        )

        self.assertIs(result, self.item)

    def test_check_availability(self):
        result = self.pharmacist.check_availability(
            self.item, 5
        )

        self.assertTrue(result)

    def test_sell_item(self):
        result = self.pharmacist.sell_item(self.item, 3)

        self.assertEqual(result, 1500)
        self.assertEqual(self.item.quantity, 7)

    def test_sale_fails_when_stock_is_insufficient(self):
        result = self.pharmacist.sell_item(self.item, 15)

        self.assertIsNone(result)
        self.assertEqual(self.item.quantity, 10)

    def test_sale_fails_for_expired_item(self):
        expired_item = Item(
            "Expired Drug",
            200,
            date.today() - timedelta(days=1),
            5
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
