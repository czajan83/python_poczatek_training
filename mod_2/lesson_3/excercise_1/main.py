import random

from shop.Order import Order
from shop.Product import Product
from shop.Apple import Apple
from shop.Potato import Potato
from shop.OrderElement import OrderElement


def excercise_4():
    product_1 = Product("jabłko", "owoce", 7)
    product_2 = Product("pomarańcza", "owoce", 11)
    product_3 = Product("ziemniak", "warzywa", 3)

    order_element_1 = OrderElement(product_1, 10)
    order_element_2 = OrderElement(product_2, 2)
    order_element_3 = OrderElement(product_3, 1)

    # order_element_1.print_order_element()
    # product_1.print_product()
    # product_2.print_product()
    # product_3.print_product()

    order_1 = Order("Andrzej", "Czajka", [order_element_1, order_element_2, order_element_3])
    order_2 = Order("Marta", "Czajka", [order_element_3])
    order_3 = Order("Gabriela", "Czajka")

    order_1.print_order()
    order_2.print_order()
    order_3.print_order()

    # products = [product_1, product_2, product_3]
    # random_product_list = []
    # for i in range(10):
    #     random_product_list.append(products[random.randint(0, 2)])
    #
    # order_4 = Order("Michał", "Wiśniewski", random_product_list)
    # order_4.print_order()


def excercise_1():
    apple_1 = Apple("Reneta", 1, 2.3)
    apple_1.calculate_full_price(3.7)

    potato_1 = Potato("Denar", 0.8, 1.9)
    potato_1.calculate_full_price(10)


if __name__ == "__main__":
    excercise_4()

# print(f"Zamówienia złożone do sklepu to: {order_1}, {order_2}, {order_3}")
#
# apple_1 = Apple("zielone_jabłko", 0.8, 16)
# apple_2 = Apple("czerwone_jabłko", 0.9, 11)
# apple_3 = Apple("antonówka", 1.1, 8.1)
#
# print(f"Jabłka dostępne w sklepie to: {apple_1}, {apple_2}, {apple_3}")
#
# potato_1 = Potato("ziemniak_jadalny", 0.45, 3.75)
# potato_2 = Potato("ziemniak_pastewny", 0.75, 0.99)
# potato_3 = Potato("sadzeniak", 0.22, 1.59)
#
# print(f"Ziemniaki dostępne w sklepie to: {potato_1}, {potato_2}, {potato_3}")
