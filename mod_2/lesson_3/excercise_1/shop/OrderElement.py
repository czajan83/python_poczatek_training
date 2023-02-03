class OrderElement:
    def __init__(self, product, amount):
        self.product = product
        self.amount = amount
        self.order_element_price = 0

    def print_order_element(self):
        print(f"Produkt: {self.product.product_name}, cena jednostkowa: {self.product.price}, ilość: {self.amount} "
              f"wartość: {self.order_element_price}")

    def calculate_order_element_price(self):
        self.order_element_price = self.amount * self.product.price
