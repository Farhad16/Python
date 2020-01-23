letters = ["a", "b", "c"]

# enumerate is a function
# it returns a enumerate object, each iteration it will return a tuple
# which is index and element of list like (0,"a")
for index, leter in enumerate(letters):
    print(index, leter)
