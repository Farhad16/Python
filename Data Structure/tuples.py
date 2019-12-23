# Normal tuple
point = 1, 2
print(point)
print(type(point))

# empty tuple
empty_tuple = ()
print(empty_tuple)
print(type(empty_tuple))

# concatination of tuple

tuple1 = (1, 3)
tuple2 = (3, 4)
result = tuple1 + tuple2
print(result)
# we can also multiply tuple
print(tuple1*3)

# we can assign tuples item in a variable
points = (11, 22, 33)
x, y, z = points
print(x)
print(y)
print(z)

# we can also print a tuple as an index number
print(points[0])

# range of tuple
print(points[0:3])
