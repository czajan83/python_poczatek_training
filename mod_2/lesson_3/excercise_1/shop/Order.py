class Order:
    def __init__(self, purchaser_name, purchaser_last_name, order_list=None):
        self.purchaser_name = purchaser_name
        self.purchaser_last_name = purchaser_last_name
        self.order_list = order_list
        if order_list is None:
            self.order_list = []
        self.whole_price = 0
        self.calculate_total_price()

    def print_order(self):
        if len(self.order_list) == 0:
            print(f"Lista zakupów użytkownika {self.purchaser_name} {self.purchaser_last_name} jest pusta")
        else:
            print(f"Lista zakupów użytkownika {self.purchaser_name} {self.purchaser_last_name} jest następująca:")
            for order_item in self.order_list:
                order_item.print_order_element()
            print(f"Łączna cena zakupów to {self.whole_price}")
            print("")

    def calculate_total_price(self):
        for order_element in self.order_list:
            order_element.calculate_order_element_price()
            self.whole_price += order_element.order_element_price
