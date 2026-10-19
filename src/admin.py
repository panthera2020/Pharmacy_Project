from customer import Customer
from user import User

class Admin(User):
    def __init__(self,name, id: int, phone_number):
        super().__init__(name, phone_number)
        self.id = id
        self.customers = []

    @property
    def id(self):
        return self.id

    @id.setter
    def id(self, number):
        self.id = number

    def add(self, customer:Customer):
        self.customers.append(customer)

    def get(self, customer_id):
        for customer in self.customers:
            if customer.id == customer_id:
                return customer
        return None