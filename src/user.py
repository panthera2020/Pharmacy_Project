from abc import ABC, abstractmethod


class User(ABC):

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