class Product:
    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value > 0:
            self.__price = value
        else:
            raise ValueError("Price can not be negative")

    def del_price(self, value):
        del self.price

    price = property(get_price, set_price, del_price)


product = Product(10)
print(product.price)
