from shop.Category import Category
from shop.Apple import Apple
from shop.Order import Order
from shop.OrderElement import OrderElement
from shop.Potato import Potato
from shop.Product import Product
from shop.SoftProduct import SoftProduct
from shop.data_generator import generate_order, add_element_to_order


def exercise_1():
    order_0 = generate_order(name="Andrzej", last_name="Czajka", length=10, discount_policy=None, discount_value=None)
    add_element_to_order(order_0)


if __name__ == "__main__":
    exercise_1()

