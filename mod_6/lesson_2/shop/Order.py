from .DiscountPolicy import PercentageDiscount, AbsoluteDiscount, DiscountPolicy
from .LimitException import LimitException


class Order:
    MAX_LENGTH = 10

    def __init__(self, purchaser_name, purchaser_last_name, order_list=None, discount_policy=None, discount_value=None):
        # discount_type = 0 ---> no discount
        # discount_type = 1 ---> 5 % of total price for habitual customers
        # discount_type = 2 ---> 20 PLN for orders with total price gt 100 PN (easter discount)
        self.__purchaser_name = purchaser_name
        self.__purchaser_last_name = purchaser_last_name
        self.order_list = order_list
        self.__whole_price_net = 0
        self.__whole_price_tax = 0
        self.__whole_price_gross = 0
        self.__discount_policy = discount_policy
        self.__discount_value = discount_value
        self.__whole_price_gross_discounted = 0

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
            raise LimitException(Order.MAX_LENGTH)
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
            return_text += f"Łączna cena zakupów to {self.whole_price_net} netto, ({self.whole_price_gross} z vat)\n"
            if self.__discount_policy is None:
                self.__discount_policy = ""
            if self.__discount_policy == "Percentage":
                discounted = PercentageDiscount(self.__whole_price_gross, self.__discount_value)
            elif self.__discount_policy == "Absolute":
                discounted = AbsoluteDiscount(self.__whole_price_gross, self.__discount_value)
            else:
                discounted = DiscountPolicy(self.__whole_price_gross)
            if self.__discount_policy == "Percentage" or self.__discount_policy == "Absolute":
                self.__whole_price_gross_discounted = discounted.apply_discount()
                if self.__whole_price_gross_discounted is not None:
                    return_text += f"Cena po uwzględnieniu rabatu wynosi {self.__whole_price_gross_discounted}"
            return return_text

    def __len__(self):
        return len(self.order_list)

    def add_product_to_order_list(self, order_element):
        if len(self.order_list) == Order.MAX_LENGTH:
            raise LimitException(Order.MAX_LENGTH,
                                 f"Osiągnięto maksymalną ilość produktów w zamówieniu ({Order.MAX_LENGTH})")
        else:
            self.order_list.append(order_element)

    def make_dictionary_for_products_in_order(self):
        products_dict_1 = {order_element.product.identifier: str(order_element.product) for order_element
                           in self.order_list}
        products_dict_2 = {order_element.product.identifier + 1: str(order_element.product) for order_element
                           in self.order_list}
        print(products_dict_1)
        print(products_dict_2)
        products_dict_1.update(products_dict_2)
        print(products_dict_1)
