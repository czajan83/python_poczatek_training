from .Order import Order
from datetime import datetime


class ExpressOrder(Order):
    def __init__(self, purchaser_name, purchaser_last_name, order_list=None, discount_policy=None, discount_value=None,
                 delivery_date=datetime.today()):
        super().__init__(purchaser_name, purchaser_last_name, order_list=order_list, discount_policy=discount_policy,
                         discount_value=discount_value)
        self.delivery_date = delivery_date

    def __str__(self):
        return_text = super().__str__()
        if self.whole_price_gross > 0:
            return return_text + f"\nPrzewidywana data dostawy to " \
                                 f"{self.delivery_date.day}.{self.delivery_date.month}.{self.delivery_date.year}\n"
