from user import User


class Admin(User):

    def __init__(self, name, admin_id, phone_number):
        super().__init__(name, phone_number)
        self._admin_id = admin_id
        self.id_number = 0

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
        return self._admin_id

    @id.setter
    def id(self, number):
        self._admin_id = number

    def register_pharmacist(self, pharmacy, pharmacist):
        if pharmacist in pharmacy.pharmacists:
            return False

        pharmacist.id = self.generate_id()
        registered = pharmacy.register_pharmacist(pharmacist)

        if registered:
            self.id_number = pharmacist.id
            return True

        pharmacist.id = None
        return False

    def remove_pharmacist(self, pharmacy, pharmacist):
        return pharmacy.remove_pharmacist(pharmacist)

    def add_stock(self, pharmacy, item):
        return pharmacy.add_item(item)

    def update_stock(self, item, quantity):
        if quantity > 0:
            item.quantity = quantity
            return True

        return False

    def get_low_stock(self, pharmacy, limit):
        low_stock = []

        for item in pharmacy.items:
            if item.quantity <= limit:
                low_stock.append(item)

        return low_stock

    def get_expired_stock(self, pharmacy):
        expired_stock = []

        for item in pharmacy.items:
            if item.is_expired():
                expired_stock.append(item)

        return expired_stock

    def generate_id(self):
        return self.id_number + 1
