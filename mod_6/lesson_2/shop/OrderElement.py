from .Product import Product
from .TaxCalculator import TaxCalculator
from dataclasses import dataclass


@dataclass
class OrderElement:
    product: Product
    amount: int
    price_net: float = 0.0
    price_tax: float = 0.0
    price_gross: float = 0.0

    def __str__(self):
        self.calculate_price_net()
        self.calculate_price_tax()
        self.calculate_price_gross()
        return f"Produkt: {self.product.name}, cena jednostkowa: {self.product.unit_price}," \
            + f"ilość: {self.amount} wartość netto: {self.price_net}," \
            + f"podatek: {self.price_tax}, wartość brutto: {self.price_gross}\n"

    def calculate_price_net(self):
        self.price_net = self.amount * self.product.unit_price

    def calculate_price_tax(self):
        self.price_tax = TaxCalculator.calculate_tax_by_product_category(self)

    def calculate_price_gross(self):
        self.price_gross = self.price_net + self.price_tax
