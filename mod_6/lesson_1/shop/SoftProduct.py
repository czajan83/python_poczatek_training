from .Product import Product
from datetime import datetime
from dataclasses import dataclass


@dataclass
class SoftProduct(Product):
    production_year: int
    years_durability: int

    def does_expire(self):
        this_year = datetime.today().year
        if this_year - self.production_year > self.years_durability:
            print(f"The durability of the product {self.name} has expired")
