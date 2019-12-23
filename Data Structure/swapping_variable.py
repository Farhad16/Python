# normal swapping
x = 10
y = 25

z = x
x = y
y = z
print("x =", x, "y = ", y)

# python swapping

x, y = y, x  # here x , y is extracting of a tuple and y,x is consider as tuple
print("x ", x)
print("y ", y)
tuple1 = x, y
a, b = tuple1
print(tuple1)
print(a)
print(b)
