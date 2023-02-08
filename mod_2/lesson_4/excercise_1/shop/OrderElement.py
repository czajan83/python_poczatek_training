class OrderElement:
    def __init__(self, product, amount):
        self.product = product
        self.amount = amount
        self.order_element_price = 0

    def __str__(self):
        return_text = f"Produkt: {self.product.name}, cena jednostkowa: {self.product.price}, "
        return return_text + f"ilość: {self.amount} " + f"wartość: {self.order_element_price}\n"

    def calculate_order_element_price(self):
        self.order_element_price = self.amount * self.product.price
