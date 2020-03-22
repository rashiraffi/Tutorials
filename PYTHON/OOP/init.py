#   All classes have a function called __init__(), which is always executed when the class is being initiated.
#   Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printf(self):
        print("Name: "+self.name+"\n"+"Age: ",self.age)


me=Person("Rashi",21)
me.printf()

#   The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
#   It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:
#class Person:
#    def __init__(this,name,age):
#        this.name=name
#        this.age=age
#    def printf(here):
#        print("Name: "+here.name+"\n"+"Age: ",here.age)

