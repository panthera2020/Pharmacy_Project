
from user import User


class Customer(User):

    def __init__(self, name, phone_number):
        super().__init__(name, phone_number)
        self._customer_id = None
        self._cart = {}

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
        return self._customer_id

    @id.setter
    def id(self, number):
        self._customer_id = number

    def search_item(self, pharmacy, name):
        return pharmacy.search_item(name)

    def add_to_cart(self, item, quantity):
        if quantity <= 0 or item.is_expired():
            return False

        if item in self._cart:
            self._cart[item] = self._cart[item] + quantity
        else:
            self._cart[item] = quantity

        return True

    def remove_from_cart(self, item):
        if item in self._cart:
            del self._cart[item]
            return True

        return False

    def update_cart_quantity(self, item, quantity):
        if item not in self._cart or quantity <= 0:
            return False

        self._cart[item] = quantity
        return True

    def get_cart_total(self):
        total = 0

        for item in self._cart:
            total = total + item.price * self._cart[item]

        return total

    def purchase(self):
        for item in self._cart:
            quantity = self._cart[item]

            if item.is_expired() or not item.is_available(quantity):
                return False

        for item in self._cart:
            item.reduce_stock(self._cart[item])

        self._cart.clear()
        return True
