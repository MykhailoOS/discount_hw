class Discount:
    def __init__(self, get_sale):
        self.get_sale = get_sale

    def discount(self):
        self.get_sale = 0.10


class RegularDiscount(Discount):

    def __init__(self, get_sale):
        super().__init__(get_sale)

    def discount(self):
        self.get_sale = 0.20


class SilverDiscount(Discount):
    def __init__(self, get_sale):
        super().__init__(get_sale)

    def discount(self):
        self.get_sale = 0.50


class GoldDiscount(Discount):

    def __init__(self, get_sale):
        super().__init__(get_sale)

    def discount(self):
        self.get_sale = 0.80


class Client:
    def __init__(self, price, name):
        self.price = price
        self.name = name

        self.discount = None

    def get_total_price(self, order: Discount):
        self.discount = self.price * order.get_sale

    def __str__(self):
        return f"Користувач {self.name};\nсума з урахуванням знижки - {self.discount}"


sale = SilverDiscount(0.20)
res = Client(8500, "Vitya")
res.get_total_price(sale)
print(res)