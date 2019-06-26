class Employee:
	def __init__(self,name,id):
		self.id=id
		self.name=name
	def display(self):
		print("ID: %d \n Name: %s"%(self.id,self.name))

emp1 = Employee("John",101)
emp2 = Employee("David",102)
emp1.display()
emp2.display()

#print the attribute name of the object emp1
print(getattr(emp1,'name'))

#reset the value of attrubute id to 105
setattr(emp1,'id',105)

emp1.display()
