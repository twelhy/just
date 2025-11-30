class Person:
	def __init__(self, name, age, size=0):
		self.name = name
		self.age = age
		self.size = size
	def pr(self):
		print(f"Your name: {self.name} \
		\nYour age: {self.age} \
		\nYour size: {self.size}")

gaz = Person("Ramazan", 15, 178)
gaz.pr()