#   A lambda function is a small anonymous function.
#   A lambda function can take any number of arguments, but can only have one expression.

x = lambda a : a + 10
print(x(5))

#   A lambda function that multiplies argument a with argument b and print the result:

y = lambda a, b : a * b
print(y(5, 6))

x1 = lambda a, b, c : a + b + c
print(x1(5, 6, 2))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))