from shop.LimitException import LimitException
from shop.Category import Category
from shop.Apple import Apple
from shop.Order import Order
from shop.OrderElement import OrderElement
from shop.Potato import Potato
from shop.Product import Product
from shop.SoftProduct import SoftProduct
from shop.data_generator import generate_order, add_element_to_order


def exercise_1():
    try:
        generate_order(name="Andrzej", last_name="Czajka", length=11, discount_policy=None, discount_value=None)
    except LimitException:
        print(f"Przykroczony limit długości zamówienia")


def exercise_2():
    try:
        generate_order(name="Andrzej", last_name="Czajka", length=11, discount_policy=None, discount_value=None)
    except LimitException as error:
        print(f"Prekroczono limit długości zamówienia wynoszący {error.allowed_limit} pozycji")


if __name__ == "__main__":
    exercise_2()

