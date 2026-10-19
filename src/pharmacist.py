from user import User

class Pharmacist(User):
    def __init__(self, name: str, id: int, phone_number: str):
        super().__init__(name, phone_number)
        self.id = id

    @property
    def id(self):
        return self.id

    @id.setter
    def id(self, number):
        self.id = number