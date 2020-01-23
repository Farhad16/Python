letters = ["a", "b", "c"]

# add in the last
letters.append("d")

# add in a specific position

letters.insert(0, "#")

# remove item
# from the last
letters.pop()
# remove using index
letters.pop(0)
# remove using items when the index is unknown
# it the remove the 1st matching item
letters.insert(0, "b")
letters.remove("b")
print(letters)

# delete a range of item

del letters[0: 2]
print(letters)

# delete all
letters.clear()
print(letters)
