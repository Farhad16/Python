# As usual syntex
points = {"x": 1, "y": 2}
print(points)

# dictionary syntex
points = dict(x=2, y=4)
print(points)

# Access a key value
print("Access ", points["x"])

# change the value of x
points["x"] = 10
points["z"] = 20
print(points)

# check if the key is exist or not
if "a" in points:
    print("Exist")
else:
    print("Not exist")
# Or use get method by default it print None
print(points.get("a"))
# or we add a value
print(points.get("a", "Not here"))

# delete a dictionary key
del points["x"]
print(points)

# in general looping
for x in points:
    print(x, points[x])

# using item method
for key, value in points.items():
    print(key, value)
