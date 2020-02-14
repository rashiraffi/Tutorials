class Animal:
	def running(self):
		print("The Animal is running...")

class Dog(Animal):
	def bark(self):
		print("The dog is barking...")

d=Dog()
d.running()
d.bark()