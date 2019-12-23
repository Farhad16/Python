numbers = [1, 1, 2, 3, 4, 4]
print(numbers)
# Now we use set , set is an unorder non duplicate list
first = set(numbers)
print(first)
second = {1, 5, 6}
# union of two sets
print("Union ", first | second)
# intersection of two sets
print("intersection ", first & second)
# difference between two sets
print("difference ", first - second)
# symmetric / protisomo difference
print("Symmetric ", first ^ second)
