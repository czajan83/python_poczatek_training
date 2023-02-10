class DiscountPolicy:
    def __init__(self, price_gross):
        self.price_gross = price_gross

    def apply_discount(self):
        return self.price_gross


class PercentageDiscount(DiscountPolicy):
    def __init__(self, price_gross, discount_percentage):
        super().__init__(price_gross)
        self.discount_percentage = discount_percentage

    def apply_discount(self):
        return self.price_gross * (1 - (self.discount_percentage / 100))


class AbsoluteDiscount(DiscountPolicy):
    def __init__(self, price_gross, discount_sum):
        super().__init__(price_gross)
        self.discount_sum = discount_sum

    def apply_discount(self):
        if self.price_gross > 10000:
            return self.price_gross - self.discount_sum
