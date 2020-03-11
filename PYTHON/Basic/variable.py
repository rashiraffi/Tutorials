#Python has no command for declaring a variable
#   A variable is created the moment you first assign a value to it.

x=6
y="Rashi"
print(x)
print(type(x))
print(y)
#   Variables do not need to be declared with any particular type and can even change type after they have been set
x=str(x)
print(type(x))

# A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)

#   Python allows you to assign values to multiple variables in one line:

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#   To combine both text and a variable, Python uses the + character:

print("I like " + x)
print("I like ",x)

#   If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function.
#   The global variable with the same name will remain as it was, global and with the original value.

#   To create a global variable inside a function, you can use the global keyword.

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)