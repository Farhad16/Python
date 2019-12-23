items = [
    ("Product1", 10),
    ("Product2", 25),
    ("Product3", 20)
]

items.sort(key=lambda item: item[1])
print(items)

a = (lambda x, y: x*y)(2, 10)
print(a)

text = (lambda me, you: me+you)("I Love ", "You")
print(text)
