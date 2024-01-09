import csv
from Item import Item

class Phone(Item):

    all = []

    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):

        # Call super function to access all attributes / methods
        super().__init__(
            name, price, quantity
        )
        
        # Item.all is a list
        Phone.all.append(self)
        
        # Run validations to received args
        assert broken_phones >= 0, f"Broken_phone is {broken_phones}, which is not >= 0."
        
        # Assign new attribute to Phone object
        self.broken_phones = broken_phones
