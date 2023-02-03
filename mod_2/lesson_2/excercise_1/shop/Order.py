class Order:
    def __init__(self, purchaser_name, purchaser_last_name, order_list=None):
        self.purchaser_name = purchaser_name
        self.purchaser_last_name = purchaser_last_name
        self.order_list = order_list
        if order_list is None:
            self.order_list = []
        self.whole_price = 0
        for order_item in self.order_list:
            self.whole_price += order_item.price

    def print_order(self):
        if len(self.order_list) == 0:
            print(f"Lista zakupów użytkownika {self.purchaser_name} {self.purchaser_last_name} jest pusta")
        else:
            print(f"Lista zakupów użytkownika {self.purchaser_name} {self.purchaser_last_name} jest następująca:")
            for order_item in self.order_list:
                order_item.print_product()


