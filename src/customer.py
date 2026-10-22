from user import User

class Customer(User):
    def __init__(self, name,phone_number):
        self._name = name
        self._phone_number = phone_number
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