class Product:
    def __init__(self, product_name, category, price):
        self.product_name = product_name
        self.category = category
        self.price = price

    def __str__(self):
        print(f"Produkt {self.product_name} należący do kategorii {self.category} "
              f"jego ceną jednostkową jest {self.price} PLN")

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        return (self.product_name == other.product_name and
                self.category == other.category and
                self.price == other.price)
