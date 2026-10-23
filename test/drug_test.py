import os
import sys

SRC_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
if SRC_PATH not in sys.path:
    sys.path.insert(0, SRC_PATH)

import unittest
from datetime import date, timedelta

from drug import Drug


class DrugTest(unittest.TestCase):

    def setUp(self):
        self.drug = Drug(
            "Paracetamol", 500, date.today() + timedelta(days=30), 10, "Tablet"
        )

    def test_drug_attributes(self):
        self.assertEqual(self.drug.name, "Paracetamol")
        self.assertEqual(self.drug.price, 500)
        self.assertEqual(self.drug.quantity, 10)
        self.assertEqual(self.drug.drug_type, "Tablet")

    def test_update_drug_type(self):
        self.drug.drug_type = "Syrup"
        self.assertEqual(self.drug.drug_type, "Syrup")

    def test_drug_inherits_stock_behaviour(self):
        self.drug.reduce_stock(2)
        self.assertEqual(self.drug.quantity, 8)


if __name__ == "__main__":
    unittest.main()
