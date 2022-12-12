class Product:

    def __init__(self, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions


class Customer:

    def __init__(self, surname, name, number):
        self.surname = surname
        self.name = name
        self.number = number


class Order:

    def __init__(self, customer, products):
        self.customer = customer
        self.product = products

    def get_order(self):
        print(self.customer.name)
        for x in self.product:
            print(x.description)

    def total(self):
        total = 0
        for x in self.product:
            total += x.price
        print(total)


phone = Product(1000, "phone", "small")
kimi = Customer("Orlova", 'Kimi', 1234)
one = Order(kimi, [phone, phone])
one.get_order()
one.total()
