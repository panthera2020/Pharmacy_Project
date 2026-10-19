from user import User

class Customer(User):
    def __init__(self, name, id: int, phone_number):
        super().__init__(name, phone_number)
        self.id = id

    @property
    def id(self):
        return self.id

    @id.setter
    def id(self, number):
        self.id = number