from user import User


class Pharmacist(User):

    def __init__(self, name, phone_number):
        super().__init__(name, phone_number)
        self._pharmacist_id = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        self._phone_number = phone_number

    @property
    def id(self):
        return self._pharmacist_id

    @id.setter
    def id(self, id_number):
        self._pharmacist_id = id_number

    def search_item(self, pharmacy, name):
        return pharmacy.search_item(name)

    def check_availability(self, item, quantity):
        return item.is_available(quantity) and not item.is_expired()

    def sell_item(self, item, quantity):
        if self.id is None:
            return None

        if self.check_availability(item, quantity):
            if item.reduce_stock(quantity):
                return item.price * quantity

        return None
