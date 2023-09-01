# Without global keyword
print("------Without global keyword(not change value using fuction)------")
x = 5
def fun():
    print("inside from the function : ",x)
fun()
print("inside from the function : ",x)

print("------Without global keyword(change value using fuction)------")
x = 5
def fun():
    x = 10
    print("inside from the function : ",x)
fun()
print("inside from the function : ",x)

# With global keyword
print("------Variable declare with global keyword(inside function)------")
def fun():
    global x
    x = 5
    print("inside from the function : ",x)
fun()
print("inside from the function : ",x)

print("------Variable declare with global keyword(inside function update value)------")
x = 5
def fun():
    global x
    x = 10
    print("inside from the function : ",x)
fun()
print("inside from the function : ",x)

# Other Example 
"""
x = 5 
def fun():
    print(x)  # give Error
    global x
    x = 10
    print(x)
fun()
print(x)
""