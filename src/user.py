from abc import ABC, abstractmethod


class User(ABC):

    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number


    @property
    @abstractmethod
    def name(self):
        ...

    @name.setter
    @abstractmethod
    def name(self, name):
        ...

    @property
    @abstractmethod
    def phone_number(self):
        ...

    @phone_number.setter
    @abstractmethod
    def phone_number(self, phone_number):
        ...
