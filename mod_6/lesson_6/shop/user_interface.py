from .errors import TemporaryOutOfStock, ProductNotAvailable, NotValidInput
from .order import Order
from .store import Store


def handle_customer():
    say_hello()
    print_previous_orders_to_user()
    order = init_order()
    while want_more_products():
        add_product_to_order(order, Store.AVAILABLE_PRODUCTS)
    print_order_summary(order)
    save_order_to_file(order)


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
    print(order)
    print("Dziękujemy i zapraszamy ponownie!")


def save_order_to_file(order):
    try:
        with open("data\\orders.txt", "a") as orders_file:
            orders_file.write(str(order))
    except IOError:
        print(f"Nie udało się zapisać zamówienia do pliku")


def print_previous_orders_to_user():
    selection = input("Czy chcesz najpierw zobaczyć historię zamówień? T/N: ")
    if selection.upper() != "T" and selection.upper() != "N":
        print("Opcje są dwie - zakładam, chcesz przejść od razu do złożenia nowego zamówienia ;)")
    if selection.upper() == "T":
        try:
            with open("data\\orders.txt", "r") as orders_file:
                print(orders_file.read())
        except IOError:
            print(f"Nie udało się odnaleźć historii zamówień")
