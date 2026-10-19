from datetime import date

class Item:
    def __init__(self, name: str, price: int, expiry_date: date):
        self.name = name
        self.price = price
        self.expiry_date = expiry_date

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, name):
        self.name = name

    @property
    def price(self):
        return self.price

    @price.setter
    def price(self, price):
        self.price = price

    @property
    def expiry_date(self):
        return self.expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        self.expiry_date = expiry_date