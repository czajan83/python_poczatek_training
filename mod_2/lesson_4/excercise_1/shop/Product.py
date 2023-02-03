class Product:
    def __init__(self, product_name, category_name, price):
        self.product_name = product_name
        self.category_name = category_name
        self.price = price

    def __str__(self):
        print(f"Produkt {self.product_name} należący do kategorii {self.category_name} "
              f"jego ceną jednostkową jest {self.price} PLN")

    def __eq__(self, other):
        return self.product_name == other.product_name and self.category_name == other.category_name and self.price == other.price
