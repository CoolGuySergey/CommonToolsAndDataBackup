

import csv


#============================================================


class Item():

    # Class attributes, global across all instances
    pay_rate = 0.8 # 20% off on everything
    all = []

    # Class method
    # Otherwise no instance on hand to call method
    @classmethod
    def instantiate_from_csv(cls):
    # cls: The class object itself is passed as first arg

        with open("Item.csv") as f:

            # Read CSV into dictionary
            reader = csv.DictReader(f)
            
            #print(reader)
            #<csv.DictReader object at 0x7fb5b3fc97c0>
            
            items = list(reader)

            for item in items:
                Item(
                    name=item.get("name"),
                    price=float(item.get("price")),
                    quantity=float(item.get("quantity")),
                )
                
            #   print(item)
            #   {'name': 'Phone', 'price': '100', 'quantity': '5'}
            #   {'name': 'Laptop', 'price': '1000', 'quantity': '3'}
            #   {'name': 'Cable', 'price': '10', 'quantity': '5'}
            #   {'name': 'Mouse', 'price': '50', 'quantity': '5'}
            #   {'name': 'Keyboard', 'price': '75', 'quantity': '5'}

    # In order to instantiate an instance succesfully
    # Name, price, and quantity must be passed
    # Constuctor: a method with a unique name and special features
    # (Used to be called magic methods)


#=====================================================================


    # Static method... all this to check if price is int??
    # Something that's related to the class but not something that's
    # unique per instance. Compare class method: manipulate different
    # structures of data to instantiate objects
    
    @staticmethod
    def is_integer(num):
    # Received parameter is regular parameter
    # Unlike other methods, not sending class reference or instance as 1st arg
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
        
        
#=====================================================================


    # Instance attributes
    def __init__(self, name: str, price: float, quantity=0):
 
        # quantity=0 comes with a default value, so doesn't need to specify typing
        # Initialise with zero in case we don't know how much we have
        # so then we can just item1 = Item("Phone", 100)
        # which will be okay, instead of item1 = Item("Phone", 100, 5)

        # Item.all is a list
        Item.all.append(self)
        
    
        # Run validations to received args
        assert price >= 0, f"Price is {price}, which is not >= 0."
        assert quantity >= 0, f"Quantity is {quantity}, which is not >= 0."
        
        # Assign to self object
        self._name = name
        self.price = price
        self.quantity = quantity
        print(f"An instance was created: {name}")

    # Read-only attributes: Restrict user to change certain attribute
    # Also known as encapsulation
    # Underscore is workaround to make self.name in constructor legal
    @property
    def name(self):
        return self._name
        
    def calculate_total_price(self):
        return self.price * self.quantity
    #python passes the object (item1) itself as the 1st argument when the method is called
    #item1.calculate_total_price() calls the method from the item1 instance

    def apply_discount(self):
        self.price = self.price * self.pay_rate
   
    def __str__(self):
        
        return f'The {self.name}s cost ${self.price} each and there are {self.quantity} of them'
    
    # Represent it in a pretty, friendly way
     
    def __repr__(self):
        
        # return f'Item({self.name}, {self.price}, {self.quantity})'
        # this will return repr(phone1) as Item(jscPhonev10, 500, 5)
        return f'{self.__class__.__name__}({self.name}, {self.price}, {self.quantity})'
        # this will return repr(phone1) as Phone(jscPhonev10, 500, 5)
        
    # Try to represent it exactly as it is created
    # Try to (if possible) use a valid python expression
    # This is the official string repr of an object
    # This needs to be UMAMBIGUOUS and is for debugging

    
