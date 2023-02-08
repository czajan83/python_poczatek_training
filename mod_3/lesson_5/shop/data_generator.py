from random import randint

from .Order import Order
from .ExpressOrder import ExpressOrder
from .OrderElement import OrderElement
from .Product import Product

MAX_QUANTITY = 100
MIN_QUANTITY = 1

PRODUCTS = [Product("jabłko", "owoce", 7),
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


def generate_order(name="Andrzej", last_name="Czajka", length=None, discount_policy=None, discount_value=None):
    if length is None:
        length = randint(1, Order.MAX_LENGTH)

    order_elements = []
    for i in range(length):
        order_elements.append(
            OrderElement(PRODUCTS[randint(0, len(PRODUCTS) - 1)], randint(MIN_QUANTITY, MAX_QUANTITY)))

    return Order(name, last_name, order_list=order_elements, discount_policy=discount_policy,
                 discount_value=discount_value)


def add_element_to_order(order):
    order.add_product_to_order_list(
        OrderElement(PRODUCTS[randint(0, len(PRODUCTS) - 1)], randint(MIN_QUANTITY, MAX_QUANTITY)))
