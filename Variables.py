# Creating Variable
x = 5 
y = "ABC"
print(x)
print(y)

# Type Casting
x = str(3)
y = int(3)
z = float(3)
print("Type Casting : ",x,y,z)

# How to know variable Datatype
print("Datatypes of x : ",type(x))
print("Datatypes of y : ",type(y))
print("Datatypes of z : ",type(z))

# for string type
x = 'ABC'
y = "ABC"    # both are valid

# Case Sensitive
a = 5 
A = 10
print("Case Sensitive : ",a,A)

# Assign Multiple Values
x,y,z = 5,10,15
print("Multiple Value : ",x,y,z)

# Assign Same Values
x = y = z = 5
print("Same Value : ",x,y,z)

# Unpack Collection
fruits = [ "Apple", "Orange","Banana" ]
x,y,z = fruits
print("Unpack Collection : ",x,y,z)

# Some Other Example
print("------Some Other Example------")
print(x,y)
print(x+y)

x = 5
print(x,y)
#print(x+y) it's give error
y = 10
print(x,y)
print(x+y)  