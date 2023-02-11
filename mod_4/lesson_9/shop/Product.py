from dataclasses import dataclass


@dataclass
class Product:
    name: str
    category: str
    unit_price: float
    identifier: int

    def __str__(self):
        return_text_1 = f"Produkt {self.name} należący do kategorii {self.category} "
        return return_text_1 + f"jego ceną jednostkową jest {self.unit_price} PLN"

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        return (self.name == other.name and
                self.category == other.category and
                self.unit_price == other.unit_price)
