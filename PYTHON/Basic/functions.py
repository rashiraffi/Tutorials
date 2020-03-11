def add(a,b):
    return(a+b)
c=5
d=6
print(add(c,d))

def wel(name):
    return("Welcome "+name+"..!")

nam="Rashi"
print(wel(nam))


#   If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

def my_function1(*kids):
  print("The youngest child is " + kids[2])

my_function1("Emil", "Tobias", "Linus")

#   If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
#   This way the function will receive a dictionary of arguments, and can access the items accordingly:

def my_function2(**kid):
  print("His last name is " + kid["lname"])

my_function2(fname = "Tobias", lname = "Refsnes")

#   The following example shows how to use a default parameter value.

def my_function3(country = "Norway"):
  print("I am from " + country)

my_function3("Sweden")
my_function3()

#   You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
def my_function4(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function4(fruits)