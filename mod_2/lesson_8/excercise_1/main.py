from shop.Apple import Apple
from shop.Order import Order
from shop.OrderElement import OrderElement
from shop.Potato import Potato
from shop.Product import Product


def take_total_price_for_order(order):
    return order.whole_price_gross


def exercise_1():
    product_1 = Product("jabłko", "owoce", 7)
    product_2 = Product("pomarańcza", "owoce", 11)
    product_3 = Product("ziemniak", "warzywa", 3)
    product_4 = Product("woda mineralna", "jedzenie", 0.99)
    product_5 = Product("mars", "jedzenie", 2.12)
    product_6 = Product("szampon", "inne", 7.13)
    product_7 = Product("okulary", "inne", 13.12)
    product_8 = Product("spodnie", "inne", 89)
    product_9 = Product("narty", "inne", 317)
    product_10 = Product("zupa", "jedzenie", 2.39)
    product_11 = Product("sok", "jedzenie", 2.99)

    order_element_1 = OrderElement(product_1, 10)
    order_element_2 = OrderElement(product_2, 2)
    order_element_3 = OrderElement(product_3, 1)
    order_element_4 = OrderElement(product_4, 1)
    order_element_5 = OrderElement(product_5, 1)
    order_element_6 = OrderElement(product_6, 1)
    order_element_7 = OrderElement(product_7, 1)
    order_element_8 = OrderElement(product_8, 1)
    order_element_9 = OrderElement(product_9, 1)
    order_element_10 = OrderElement(product_10, 1)
    order_element_11 = OrderElement(product_11, 1)

    order_1 = Order("Andrzej", "Czajka", [order_element_1, order_element_2, order_element_3, order_element_4,
                                                     order_element_5, order_element_6, order_element_7, order_element_8,
                                                     order_element_9, order_element_10, order_element_11])
    order_2 = Order("Marta", "Czajka", [order_element_3, order_element_2, order_element_4, order_element_7])
    order_3 = Order("Gabriela", "Czajka", [order_element_7, order_element_1, order_element_9])
    order_4 = Order("Iga", "Giemzik", [order_element_2, order_element_11, order_element_1, order_element_5])
    order_5 = Order("Elżbieta", "Gołowkin", [order_element_2, order_element_3, order_element_8, order_element_10])

    orders = [order_1, order_2, order_3, order_4, order_5]

    for order in orders:
        print(order)

    orders.sort(key=lambda order: order.whole_price_gross)
    print(f"\n=================================================================\n")

    for order in orders:
        print(order)


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
    product_3 = Product("jabłko", "owoce", 7)
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
