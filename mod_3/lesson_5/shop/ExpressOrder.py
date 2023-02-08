from .Order import Order
from datetime import datetime


class ExpressOrder(Order):
    def __init__(self, purchaser_name, purchaser_last_name, order_list=None, delivery_date=datetime.today()):
        super().__init__(purchaser_name, purchaser_last_name, order_list)
        self.delivery_date = delivery_date

    def __str__(self):
        if len(self.order_list) == 0:
            return f"Lista zakupów użytkownika {self.purchaser_name} {self.purchaser_last_name} jest pusta"
        else:
            return_text = f"Lista zakupów użytkownika {self.purchaser_name} {self.purchaser_last_name} "
            return_text += f"jest następująca:\n"
            for order_item in self.order_list:
                return_text += str(order_item)
            return return_text + f"Łączna cena zakupów to {self.whole_price_net} netto, ({self.whole_price_gross}" \
                                 f" z vat), przewidywana data dostawy to " \
                                 f"{self.delivery_date.day}.{self.delivery_date.month}.{self.delivery_date.year}\n"
