
from datetime import date


class Item:

    def __init__(self, name, price, expiry_date, quantity):
        self._name = name
        self._price = price
        self._expiry_date = expiry_date
        self._quantity = quantity

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

    @property
    def expiry_date(self):
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        self._expiry_date = expiry_date

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        self._quantity = quantity

    def is_expired(self):
        return self.expiry_date < date.today()

    def is_available(self, quantity):
        return quantity > 0 and self.quantity >= quantity

    def reduce_stock(self, quantity):
        if self.is_available(quantity):
            self.quantity = self.quantity - quantity
            return True

        return False

    def increase_stock(self, quantity):
        if quantity > 0:
            self.quantity = self.quantity + quantity
            return True

        return False
