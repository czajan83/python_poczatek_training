class Product:
    def __init__(self, product_name, category_name, price):
        self.product_name = product_name
        self.category_name = category_name
        self.price = price

    def print_product(self):
        print(f"Produkt {self.product_name} należący do kategorii {self.category_name} "
              f"jego ceną jednostkową jest {self.price} PLN")


