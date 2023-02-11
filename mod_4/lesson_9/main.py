from shop.Apple import Apple
from shop.Order import Order
from shop.OrderElement import OrderElement
from shop.Potato import Potato
from shop.Product import Product
from shop.SoftProduct import SoftProduct
from shop.data_generator import generate_order, add_element_to_order


def take_total_price_for_order(order):
    return order.whole_price_gross


def test_product__eq__method(product_1_data, product_2_data, expected_result):
    product_1 = Product(*product_1_data)
    product_2 = Product(*product_2_data)
    if (product_1 == product_2) == expected_result:
        print("Test passed")
    else:
        print("Test failed")


def exercise_1():
    test_product__eq__method(("jabłko", "owoce", 45, 2222), ("jabłko", "owoce", 45, 3335), True)
    test_product__eq__method(("jabłko", "owoce", 45, 3333), ("jabłko", "owoce", 45, 3335), False)
    test_product__eq__method(("jabłko", "owoce", 45, 3333), ("gruszka", "owoce", 45, 3335), True)
    test_product__eq__method(("jabłko", "owoce", 45, 3333), ("gruszka", "owoce", 45, 3335), False)


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
