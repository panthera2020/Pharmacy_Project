
class Pharmacy:

    def __init__(self):
        self.items = []
        self.pharmacists = []

    def add_item(self, item):
        if item not in self.items:
            self.items.append(item)
            return True

        return False

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            return True

        return False

    def search_item(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                return item

        return None

    def register_pharmacist(self, pharmacist):
        if pharmacist not in self.pharmacists:
            self.pharmacists.append(pharmacist)
            return True

        return False

    def remove_pharmacist(self, pharmacist):
        if pharmacist in self.pharmacists:
            self.pharmacists.remove(pharmacist)
            return True

        return False
