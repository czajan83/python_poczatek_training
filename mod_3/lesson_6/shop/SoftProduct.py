from .Product import Product
from datetime import datetime


class SoftProduct(Product):
    def __init__(self, name, category, price, production_year, years_durability):
        super().__init__(name, category, price)
        self.production_year = production_year
        self.years_durability = years_durability

    def does_expire(self):
        this_year = datetime.today().year
        if this_year - self.production_year > self.years_durability:
            print(f"The durability of the product {self.name} has expired")
