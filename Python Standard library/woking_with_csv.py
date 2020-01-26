import csv

# with open("data.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerow(["ProductId", "ProductName", "Price"])
#     writer.writerow([1001, "Pant", 1500])
#     writer.writerow([1002, "Shirt", 1000])

with open("data.csv") as file:
    reader = csv.reader(file)
    for read in reader:
        print(read)
