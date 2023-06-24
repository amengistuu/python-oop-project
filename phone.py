from item import Item

class Phone(Item): 
	# it is a good idea to to removing original attributes in the child-class level, because the super function in the child access helps us access the parent's attribute
	def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
		# call to super function to have access to all of attributes and methods that are coming from the class we inherit from 
		super().__init__(
			name, price, quantity
		)

		# run validations to the received arguments
		assert broken_phones >= 0, f'Broken phones {broken_phones} is not greater than or equal to zero'

		# assign to self object
		self.broken_phones = broken_phones

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
	
	# static methods are not sending the instance as a first method, unlike the class methods. It is like a regular function that receives paramters.
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