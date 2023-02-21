import csv
import random

from .errors import TemporaryOutOfStock, ProductNotAvailable
from .product import Product, ProductCategory


class AvailableProduct:

    def __init__(self, quantity, name, category, unit_price=None, identifier=None):
        if unit_price is None:
            unit_price = random.randint(1, 100)
        if identifier is None:
            identifier = random.randint(1, 100)

        self.quantity = quantity
        self.product = Product(name=name, category=category, unit_price=unit_price, identifier=identifier)


class Store:
    AVAILABLE_PRODUCTS = None

    @staticmethod
    def reserve_product(product, quantity):
        for index, available_product in enumerate(Store.AVAILABLE_PRODUCTS):
            if available_product.product == product:
                if available_product.quantity < quantity:
                    raise TemporaryOutOfStock(available_product.product.name, available_product.quantity)
                else:
                    Store.AVAILABLE_PRODUCTS[index].quantity = available_product.quantity - quantity
                break
        else:
            raise ProductNotAvailable(f"Brak produktu w ofercie sklepu")

    @staticmethod
    def load_store_stock():
        success = False
        try:
            with open(f"data\\stock.csv", newline="\n") as stock_data_file:
                stock_data = csv.DictReader(stock_data_file, delimiter=";")
                headers = stock_data.fieldnames
                Store.AVAILABLE_PRODUCTS = []
                for line in stock_data:
                    quantity = int(line[headers[0]])
                    name = line[headers[1]]
                    if line[headers[2]] == "0":
                        category = ProductCategory.FOOD
                    elif line[headers[2]] == "1":
                        category = ProductCategory.TOOLS
                    else:
                        category = ProductCategory.OTHER
                    Store.AVAILABLE_PRODUCTS.append(AvailableProduct(quantity, name, category))
            success = True
        except IOError():
            print("Nie udało się wczytać stanu magazynowego sklepu")
            success = False
        finally:
            return success

    @staticmethod
    def save_store_stock():
        try:
            with open(f"data\\stock1.csv", mode="w", newline="\n") as stock_data_file:
                headers = ["quantity", "name", "category"]
                stock_data = csv.DictWriter(stock_data_file, delimiter=";", fieldnames=headers)
                stock_data.writeheader()
                for entry in Store.AVAILABLE_PRODUCTS:
                    if entry.product.category == ProductCategory.FOOD:
                        category = "0"
                    elif entry.product.category == ProductCategory.TOOLS:
                        category = "1"
                    else:
                        category = "2"
                    stock_data.writerow({
                        "quantity": str(entry.quantity),
                        "name": entry.product.name,
                        "category": category
                    })
        except IOError():
            print("Nie udało się zapisać stanu magazynowego sklepu")
