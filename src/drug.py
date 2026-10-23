
from item import Item


class Drug(Item):

    def __init__(self, name, price, expiry_date, quantity, drug_type):
        super().__init__(name, price, expiry_date, quantity)
        self._drug_type = drug_type

    @property
    def drug_type(self):
        return self._drug_type

    @drug_type.setter
    def drug_type(self, drug_type):
        self._drug_type = drug_type
