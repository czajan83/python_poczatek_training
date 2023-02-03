class Order:
    def __init__(self, purchaser_name, purchaser_last_name, order_list=None):
        self.purchaser_name = purchaser_name
        self.purchaser_last_name = purchaser_last_name
        self.order_list = order_list
        if order_list is None:
            self.order_list = []
        self.whole_price = 0
        self.calculate_total_price()

    def __str__(self):
        if len(self.order_list) == 0:
            return f"Lista zakupów użytkownika {self.purchaser_name} {self.purchaser_last_name} jest pusta"
        else:
            return_text = f"Lista zakupów użytkownika {self.purchaser_name} {self.purchaser_last_name} "
            return_text += f"jest następująca:\n"
            for order_item in self.order_list:
                return_text += str(order_item)
            return return_text + f"Łączna cena zakupów to {self.whole_price}\n"

    def __len__(self):
        return len(self.order_list)

    def calculate_total_price(self):
        for order_element in self.order_list:
            order_element.calculate_order_element_price()
            self.whole_price += order_element.order_element_price
