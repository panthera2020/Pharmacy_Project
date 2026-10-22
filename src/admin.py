from user import User

class Admin(User):
    def __init__(self,name, admin_id: int, phone_number):
        self._name = name
        self._phone_number = phone_number
        self._admin_id = admin_id

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
        return self._id

    @id.setter
    def id(self, number):
        self._id = number