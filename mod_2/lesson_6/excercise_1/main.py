from shop.Apple import Apple
from shop.Order import Order
from shop.OrderElement import OrderElement
from shop.Potato import Potato
from shop.Product import Product


def excercise_1():
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

    # order_element_1.print_order_element()
    # product_1.print_product()
    # product_2.print_product()
    # product_3.print_product()

    order_1 = Order("Andrzej", "Czajka", [order_element_1, order_element_2, order_element_3, order_element_4,
                                          order_element_5, order_element_6, order_element_7, order_element_8,
                                          order_element_9, order_element_10, order_element_11])
    # order_2 = Order("Marta", "Czajka", [order_element_3])
    # order_3 = Order("Gabriela", "Czajka")

    print(str(order_1))
    # print(str(order_2))
    # print(str(order_3))

    order_1.add_product_to_order_list(order_element_4)

    print(str(order_1))

    # products = [product_1, product_2, product_3]
    # random_product_list = []
    # for i in range(10):
    #     random_product_list.append(products[random.randint(0, 2)])
    #
    # order_4 = Order("Michał", "Wiśniewski", random_product_list)
    # order_4.print_order()


def excercise_2():
    apple_1 = Apple("Reneta", 1, 2.3)
    apple_1.calculate_full_price(3.7)
    print(str(apple_1))

    potato_1 = Potato("Denar", 0.8, 1.9)
    potato_1.calculate_full_price(10)
    print(str(potato_1))


def excercise_3():
    product_1 = Product("jabłko", "owoce", 7)
    product_2 = Product("pomarańcza", "owoce", 11)
    product_3 = Product("ziemniak", "warzywa", 3)

    order_element_1 = OrderElement(product_1, 10)
    order_element_2 = OrderElement(product_2, 2)
    order_element_3 = OrderElement(product_3, 1)

    order_1 = Order("Andrzej", "Czajka", [order_element_1, order_element_2, order_element_3, order_element_1])
    print(str(len(order_1)))


def excercise_4():
    product_1 = Product("jabłko", "owoce", 7)
    product_2 = Product("jabłko", "owoce", 6)
    product_3 = Product("jabłko", "owoce", 7)
    potato_1 = Potato("Denar", 0.8, 1.9)
    print(f"{product_1 == product_2}")
    print(f"{product_1 == potato_1}")


if __name__ == "__main__":
    excercise_1()

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
