from shop.TaxCalculator import TaxCalculator


class OrderElement:
    def __init__(self, product, amount):
        self.product = product
        self.amount = amount
        self.order_element_price_net = 0
        self.order_element_price_tax = 0
        self.order_element_price_gross = 0

    def __str__(self):
        self.calculate_order_element_price_net()
        self.calculate_order_element_price_tax()
        self.calculate_order_element_price_gross()
        return f"Produkt: {self.product.product_name}, cena jednostkowa: {self.product.price}," \
            + f"ilość: {self.amount} wartość netto: {self.order_element_price_net}," \
            + f"podatek: {self.order_element_price_tax}, wartość brutto: {self.order_element_price_gross}\n"

    def calculate_order_element_price_net(self):
        self.order_element_price_net = self.amount * self.product.price

    def calculate_order_element_price_tax(self):
        self.order_element_price_tax = TaxCalculator.calculate_tax_by_product_category(self)

    def calculate_order_element_price_gross(self):
        self.order_element_price_gross = self.order_element_price_net + self.order_element_price_tax
