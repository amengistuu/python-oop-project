import csv

class Item:
    pay_rate = 0.8 # the pay rate after 20% discount
    all =[]
    def __init__(self, name: str, price: float, quantity=0):
        # you can dynamically assign an attribute to an instance
        # run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero."
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero."

        # assign to self object
        self.__name = name
        self.price = price
        self.quantity = quantity

        # actions to execute
        Item.all.append(self) 

    @property
    # property decorator = read-only attribute
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 25:
            raise Exception("The name is too long!")
        else:
            self.__name = value
        self.__name = value

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate
    # this method is designed for instantiating the object itself, so it can not be called from the instance itself
    # this method needs to be converted to a class method w/ a decarator 

    @classmethod
    def instantiate_from_csv(cls): # the class method must receive the class itself as an argument (labeled 'cls' instead of 'self' for less confusion)
        # using context manager - no need to close file
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    # static methods are not sending the instance as a first input, unlike the class methods. It is like a regular function that receives paramters.
    @staticmethod
    def is_integer(num):
        # we will count out the floats that are point zero
        # for example, 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        # return the object in the same way we create them - this is best practice
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"