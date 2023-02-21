from random import randint

from .Category import Category
from .Order import Order
from .ExpressOrder import ExpressOrder
from .OrderElement import OrderElement
from .Product import Product

MAX_QUANTITY = 100
MIN_QUANTITY = 1

PRODUCTS = [Product("jabłko", Category.FRUITS, 7, randint(1, 10000)),
            Product("pomarańcza", Category.FRUITS, 11, randint(1, 10000)),
            Product("ziemniak", Category.VEGETABLES, 3, randint(1, 10000)),
            Product("woda mineralna", Category.FOOD, 0.99, randint(1, 10000)),
            Product("mars", Category.FOOD, 2.12, randint(1, 10000)),
            Product("szampon", Category.OTHERS, 7.13, randint(1, 10000)),
            Product("okulary", Category.OTHERS, 13.12, randint(1, 10000)),
            Product("spodnie", Category.OTHERS, 89, randint(1, 10000)),
            Product("narty", Category.OTHERS, 317, randint(1, 10000)),
            Product("zupa", Category.FOOD, 2.39, randint(1, 10000)),
            Product("sok", Category.FOOD, 2.99, randint(1, 10000))]


def generate_order(name="Andrzej", last_name="Czajka", length=None, discount_policy=None, discount_value=None):
    if length is None:
        length = randint(1, Order.MAX_LENGTH)

    order_elements = []
    for i in range(length):
        order_elements.append(
            OrderElement(PRODUCTS[randint(0, len(PRODUCTS) - 1)], randint(MIN_QUANTITY, MAX_QUANTITY)))

    return ExpressOrder(name, last_name, order_list=order_elements, discount_policy=discount_policy,
                        discount_value=discount_value)


def add_element_to_order(order):
    order.add_product_to_order_list(
        OrderElement(PRODUCTS[randint(0, len(PRODUCTS) - 1)], randint(MIN_QUANTITY, MAX_QUANTITY)))
