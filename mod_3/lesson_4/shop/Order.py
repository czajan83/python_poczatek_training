class Order:
    MAX_LENGTH = 10

    def __init__(self, purchaser_name, purchaser_last_name, order_list=None):
        # discount_type = 0 ---> no discount
        # discount_type = 1 ---> 5 % of total price for habitual customers
        # discount_type = 2 ---> 20 PLN for orders with total price gt 100 PN (easter discount)
        self.__purchaser_name = purchaser_name
        self.__purchaser_last_name = purchaser_last_name
        self.order_list = order_list
        self.__whole_price_net = 0
        self.__whole_price_tax = 0
        self.__whole_price_gross = 0

    @property
    def purchaser_name(self):
        return self.__purchaser_name

    @property
    def purchaser_last_name(self):
        return self.__purchaser_last_name

    @property
    def whole_price_net(self):
        self.__whole_price_net = 0
        for order_element in self.__order_list:
            order_element.calculate_order_element_price_net()
            self.__whole_price_net += order_element.order_element_price_net
        return self.__whole_price_net

    @property
    def whole_price_tax(self):
        self.__whole_price_tax = 0
        for order_element in self.__order_list:
            order_element.calculate_order_element_price_tax()
            self.__whole_price_tax += order_element.order_element_price_tax
        return self.__whole_price_tax

    @property
    def whole_price_gross(self):
        self.__whole_price_gross = 0
        for order_element in self.__order_list:
            order_element.calculate_order_element_price_gross()
            self.__whole_price_gross += order_element.order_element_price_gross
        return self.__whole_price_gross

    @property
    def order_list(self):
        return self.__order_list

    @order_list.setter
    def order_list(self, value=None):
        if value is None:
            self.__order_list = []
        elif len(value) > Order.MAX_LENGTH:
            self.__order_list = value[:Order.MAX_LENGTH]
        else:
            self.__order_list = value

    def __str__(self):
        if len(self.order_list) == 0:
            return f"Lista zakupów użytkownika {self.purchaser_name} {self.purchaser_last_name} jest pusta"
        else:
            return_text = f"Lista zakupów użytkownika {self.purchaser_name} {self.purchaser_last_name} "
            return_text += f"jest następująca:\n"
            for order_item in self.order_list:
                return_text += str(order_item)
            return_text += f"Łączna cena zakupów to {self.whole_price_net} netto, ({self.whole_price_gross} z vat)"
            return return_text + "\n"

    def __len__(self):
        return len(self.order_list)

    def add_product_to_order_list(self, order_element):
        if len(self.order_list) == Order.MAX_LENGTH:
            print(f"Maksymalna ilość produktów w zamówieniu: {Order.MAX_LENGTH} została przekroczona")
        else:
            self.order_list.append(order_element)
