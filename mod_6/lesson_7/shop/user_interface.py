import json
import random
import os

from .errors import TemporaryOutOfStock, ProductNotAvailable, NotValidInput
from .order import Order
from .store import Store


def handle_customer():
    say_hello()
    print_previous_orders_to_user()
    # order = init_order()
    # while want_more_products():
    #     add_product_to_order(order, Store.AVAILABLE_PRODUCTS)
    # print_order_summary(order)
    # save_order_to_file(order)


def load_stock():
    return Store.load_store_stock()


def save_stock():
    Store.save_store_stock()


def say_hello():
    print("Witaj w naszym sklepie!")


def init_order():
    name = input("Podaj swoje imię ")
    last_name = input("Podaj nazwisko ")
    return Order(name, last_name)


def want_more_products():
    selection = input("Czy chcesz dodać produkty do zamówienia? T/N: ")
    if selection.upper() != "T" and selection.upper() != "N":
        print("Opcje są dwie - zakładam, że chcesz coś zamówić ;)")
        return True
    return selection.upper() == "T"


def add_product_to_order(order, available_products):
    print("Oto dostępne produkty:")
    for index, available_product in enumerate(available_products):
        print(f"{index}) {available_product.product}")

    try:
        product_index_str = input("Wybierz numer: ")
        product_index = parse_product_index(product_index_str, max_index=len(available_products) - 1)

        quantity_str = input("Podaj liczbę sztuk: ")
        quantity = parse_quantity(quantity_str)
    except NotValidInput as input_error:
        print(f"{input_error}")

    try:
        order.add_product_to_order(available_products[product_index].product, quantity)
    except TemporaryOutOfStock as error:
        print(f"Niestety mamy dostępne tylko {error.available_quantity} sztuk produktu {error.product_name}")
    except ProductNotAvailable as error:
        print(f"Produkt {error.product_name} nie jest dostępny. Wybierz inny.")
    except UnboundLocalError:
        pass


def parse_product_index(product_index_str, max_index):
    if product_index_str.lstrip("-").isnumeric() is not True:
        raise NotValidInput("Nie rozpoznano liczby. Należało podać numer pozycji")
    if int(product_index_str) < 0 or int(product_index_str) > max_index:
        raise NotValidInput("Nie znaleziono pozycji na liście")
    return int(product_index_str)


def parse_quantity(quantity_str):
    if quantity_str.lstrip("-").isnumeric() is not True:
        raise NotValidInput("Nie rozpoznano liczby. Należało podać liczbę określającą ilość sztuk wybranego produktu")
    if int(quantity_str) < 0:
        raise NotValidInput("Podano ujemną ilość sztuk wybranego produktu")
    return int(quantity_str)


def print_order_summary(order):
    print("Twoje zamówienie to:")
    print(order.format_as_dict())
    print("Dziękujemy i zapraszamy ponownie!")


def save_order_to_file(order):
    try:
        file_size = os.stat("data\\orders.json").st_size
    except FileNotFoundError:
        file_size = 0
    if file_size == 0:
        orders_as_dict = {f"order_id_{random.randint(0, 10000)}": order.format_as_dict()}
    else:
        try:
            with open("data\\orders.json", "r") as orders_file:
                orders_as_dict = json.load(orders_file)
                orders_as_dict.update(
                    {f"order_id_{random.randint(0, 10000)}": order.format_as_dict()})
        except IOError:
            print(f"Nie udało się zaktualizować zamówienia do pliku")
    try:
        with open("data\\orders.json", "w") as orders_file:
            json.dump(orders_as_dict, orders_file, indent=4)
    except IOError:
        print(f"Nie udało się dopisać zamówienia do pliku")


def print_previous_orders_to_user():
    try:
        with open("data\\orders.json", "r") as orders_file:
            orders_dict = json.load(orders_file)
    except IOError:
        orders_dict = {}
    print("Ten program wyświetli identyfikatory twoich zakupów")
    name = input("Podaj swoje imię: ")
    last_name = input("Podaj swoje nazwisko: ")
    for order_key in list(orders_dict):
        if orders_dict[order_key][f"client_name"] == name and orders_dict[order_key][f"client_last_name"] == last_name:
            print(order_key)
