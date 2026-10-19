

class User:
    def __init__(self, name: str, phone_number: str):
        self.name = name
        self.phone_number = phone_number

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, name):
        self.name = name

    @property
    def phone_number(self):
        return self.phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        self.phone_number = phone_number