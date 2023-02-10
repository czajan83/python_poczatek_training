class Product:
    def __init__(self, name, category, price, identifier):
        self.name = name
        self.category = category
        self.price = price
        self.identifier = identifier

    def __str__(self):
        return_text_1 = f"Produkt {self.name} należący do kategorii {self.category} "
        return return_text_1 + f"jego ceną jednostkową jest {self.price} PLN"

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        return (self.name == other.name and
                self.category == other.category and
                self.price == other.price)
