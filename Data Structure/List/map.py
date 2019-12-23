items = [
    ("Product1", 10),
    ("Product2", 25),
    ("Product3", 20)
]

# normal process of finding price list
prices = []

for item in items:
    prices.append(item[1])

print(prices)

# using map find the prices

x = map(lambda item: item[1], items)
for price in x:
    print(price)

# find the list of prices using list and lambda

x = list(map(lambda item: item[1], items))
print(x)


# example of map and calcule the total price of the products

price = list(map(lambda item: item[1], items))
product = list(map(lambda item: item[0], items))
sum = 0
for x in price:
    sum = sum + x
print(sum)
print(product)
