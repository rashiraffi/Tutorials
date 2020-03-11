#   Text Type:	    str
#   Numeric Types:	int, float, complex
#   Sequence Types:	list, tuple, range
#   Mapping Type:	dict
#   Set Types:	    set, frozenset
#   Boolean Type:	bool
#   Binary Types:	bytes, bytearray, memoryview

#   Print the data type of the variable x:
x = 5
print(x,"Is a",type(x))
x = ["apple", "banana", "cherry"]
print(x,"Is a",type(x))
x = ("apple", "banana", "cherry")
print(x , "Is a",type(x))
x = {"name" : "John", "age" : 36}
print(x , "Is a",type(x))
x = {"apple", "banana", "cherry"}
print(x , "Is a",type(x))
x = frozenset({"apple", "banana", "cherry"})
print(x , "Is a",type(x))
x = True
print(x , "Is a",type(x))
x = b"Hello"
print(x,"Is a",type(x))
x = bytearray(5)
print(x,"Is a",type(x))
x = memoryview(bytes(5))
print(x,"Is a",type(x))

x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))


x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))


#   int() - constructs an integer number from an integer literal, a float literal (by rounding down to the previous whole number), 
#       or a string literal (providing the string represents a whole number)
#   float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
#   str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals