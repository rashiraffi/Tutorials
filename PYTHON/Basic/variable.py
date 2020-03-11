#Python has no command for declaring a variable
#A variable is created the moment you first assign a value to it.

x=6
y="Rashi"
print(x)
print(type(x))
print(y)
#Variables do not need to be declared with any particular type and can even change type after they have been set
x=str(x)
print(type(x))

# A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)