letters = ["a", "b", "c", "d"]
# assign a new value in the list 1st index
letters[0] = "A"
print(letters)

# print a length of the list 0 to 3 means it print 1st three elements of list
print(letters[0:3])

# we can also print a range wise elements
print(letters[::2])

# range of list

numbers = list(range(0, 20))
print(numbers)
# now we need to print the reverse of the numbers
print(numbers[::-1])  # start from : to : increment of decrement

# or
print(numbers[20:0:-1])


# even numbers of the list
print(numbers[::2])

# odd numbers of the list
print(numbers[1::2])
