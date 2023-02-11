class TaxCalculator:
    __LEVEL_1 = 5
    __LEVEL_2 = 8
    __LEVEL_3 = 20

    @staticmethod
    def calculate_tax_by_product_category(order_element):
        if order_element.product.category == "owoce" or order_element.product.category == "warzywa":
            tax_level = TaxCalculator.__LEVEL_1
        elif order_element.product.category == "jedzenie":
            tax_level = TaxCalculator.__LEVEL_2
        else:
            tax_level = TaxCalculator.__LEVEL_3
        return (tax_level / 100) * order_element.order_element_price_net

