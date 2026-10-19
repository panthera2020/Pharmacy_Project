import admin
import pharmacist


class Pharmacy:
    def __init__(self):
        self.drugs = []
        self.items = []
        self.admin = admin
        self.pharmacist = pharmacist
