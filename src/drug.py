from item import Item


class Drug(Item):
    def __init__(self, name, price, expiry_date):
        super().__init__(name, price, expiry_date)

    