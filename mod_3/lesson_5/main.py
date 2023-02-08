from shop.Apple import Apple
from shop.Order import Order
from shop.OrderElement import OrderElement
from shop.Potato import Potato
from shop.Product import Product
from shop.SoftProduct import SoftProduct
from shop.data_generator import generate_order, add_element_to_order


def take_total_price_for_order(order):
    return order.whole_price_gross


def exercise_1():
    # soft_product_1 = SoftProduct("aaa", "bbb", 2.1, 1992, 30)
    # soft_product_2 = SoftProduct("ccc", "ddd", 2.1, 1993, 30)
    # soft_product_3 = SoftProduct("eee", "fff", 2.1, 1994, 30)
    #
    # soft_product_1.does_expire()
    # soft_product_2.does_expire()
    # soft_product_3.does_expire()

    order = generate_order(length=5, discount_policy="Percentage", discount_value=5)
    print(order)

    # add_element_to_order(order)
    # print(order)
    #
    # add_element_to_order(order)
    # print(order)


def exercise_2():
    apple_1 = Apple("Reneta", 1, 2.3)
    apple_1.calculate_full_price(3.7)
    print(str(apple_1))

    potato_1 = Potato("Denar", 0.8, 1.9)
    potato_1.calculate_full_price(10)
    print(str(potato_1))


def exercise_3():
    product_1 = Product("jabłko", "owoce", 7)
    product_2 = Product("pomarańcza", "owoce", 11)
    product_3 = Product("ziemniak", "warzywa", 3)

    order_element_1 = OrderElement(product_1, 10)
    order_element_2 = OrderElement(product_2, 2)
    order_element_3 = OrderElement(product_3, 1)

    order_1 = Order("Andrzej", "Czajka", [order_element_1, order_element_2, order_element_3, order_element_1])
    print(str(len(order_1)))


def exercise_4():
    product_1 = Product("jabłko", "owoce", 7)
    product_2 = Product("jabłko", "owoce", 6)
    potato_1 = Potato("Denar", 0.8, 1.9)
    print(f"{product_1 == product_2}")
    print(f"{product_1 == potato_1}")


if __name__ == "__main__":
    exercise_1()

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
