from random import randint

from mod_3.lesson_1.shop.Order import Order
from mod_3.lesson_1.shop.OrderElement import OrderElement
from mod_3.lesson_1.shop.Product import Product

MAX_QUANTITY = 100
MIN_QUANTITY = 1


def generate_order(name="Andrzej", last_name="Czajka", length=None):
    products = [Product("jabłko", "owoce", 7),
                Product("pomarańcza", "owoce", 11),
                Product("ziemniak", "warzywa", 3),
                Product("woda mineralna", "jedzenie", 0.99),
                Product("mars", "jedzenie", 2.12),
                Product("szampon", "inne", 7.13),
                Product("okulary", "inne", 13.12),
                Product("spodnie", "inne", 89),
                Product("narty", "inne", 317),
                Product("zupa", "jedzenie", 2.39),
                Product("sok", "jedzenie", 2.99)]

    if length is None:
        length = randint(1, Order.MAX_LENGTH)

    order_elements = []
    for i in range(length):
        order_elements.append(OrderElement(products[randint(0, len(products)-1)], randint(MIN_QUANTITY, MAX_QUANTITY)))

    return Order(name, last_name, order_elements)
