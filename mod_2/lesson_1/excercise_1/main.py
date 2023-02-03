class Product:
    pass


class Order:
    pass


class Apple:
    pass


class Potato:
    pass


green_apple = Apple()
red_apple = Apple()

old_potato = Potato()
young_potato = Potato()

print(f"type of green apple is {type(green_apple)}")
print(f"type of red apple is {type(red_apple)}")

print(f"type of old potato is {type(old_potato)}")
print(f"type of young potato is {type(young_potato)}")

order_list1 = [Order(), Order(), Order(), Order(), Order()]
products = {"apple": Product(), "potato": Product(), }

print(order_list1)
print(products)
