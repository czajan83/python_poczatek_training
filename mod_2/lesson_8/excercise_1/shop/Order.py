class Order:
    __MAX_LENGTH = 10

    def __init__(self, purchaser_name, purchaser_last_name, order_list=None):
        # discount_type = 0 ---> no discount
        # discount_type = 1 ---> 5 % of total price for habitual customers
        # discount_type = 2 ---> 20 PLN for orders with total price gt 100 PN (easter discount)
        self.purchaser_name = purchaser_name
        self.purchaser_last_name = purchaser_last_name
        if order_list is None:
            self.__order_list = []
        elif len(order_list) > Order.__MAX_LENGTH:
            self.__order_list = order_list[:Order.__MAX_LENGTH]
        else:
            self.__order_list = order_list
        self.whole_price_net = 0
        self.whole_price_tax = 0
        self.whole_price_gross = 0
        self.__calculate_total_price()

    def __str__(self):
        if len(self.__order_list) == 0:
            return f"Lista zakupów użytkownika {self.purchaser_name} {self.purchaser_last_name} jest pusta"
        else:
            return_text = f"Lista zakupów użytkownika {self.purchaser_name} {self.purchaser_last_name} "
            return_text += f"jest następująca:\n"
            for order_item in self.__order_list:
                return_text += str(order_item)
            return_text += f"Łączna cena zakupów to {self.whole_price_net} netto, ({self.whole_price_gross} z vat)\n"
            return return_text

    def __len__(self):
        return len(self.__order_list)

    def __calculate_total_price(self):
        self.whole_price_net = 0
        for order_element in self.__order_list:
            order_element.calculate_order_element_price_net()
            order_element.calculate_order_element_price_tax()
            order_element.calculate_order_element_price_gross()
            self.whole_price_net += order_element.order_element_price_net
            self.whole_price_tax += order_element.order_element_price_tax
            self.whole_price_gross += order_element.order_element_price_gross

    def add_product_to_order_list(self, order_element):
        if len(self.__order_list) == Order.__MAX_LENGTH:
            print(f"Maksymalna ilość produktów w zamówieniu: {Order.__MAX_LENGTH} została przekroczona")
        else:
            self.__order_list.append(order_element)
            self.__calculate_total_price()

    @classmethod
    def change_max_length(cls, new_max_length):
        cls.__MAX_LENGTH == new_max_length
