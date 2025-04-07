# functools.singledispatch

from pprint import pprint
from functools import singledispatch


def main():
    item = {
        "name": "item1",
        "price": 300,
        "quantity": 2,
    }

    discount_type = DiscountTypeBOGO()
    discount = calculate_discount(discount_type, item)
    discount_description = make_discount_description(discount_type, item)

    pprint(
        item
        | {
            "discount_type": discount_type,
            "discount_amount": discount,
            "discount_description": discount_description,
        },
        sort_dicts=False,
    )


class DiscountTypeBase:
    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"


class DiscountTypePercent(DiscountTypeBase):
    def __init__(self, percent):
        self.percent = percent


class DiscountTypeFlat(DiscountTypeBase):
    def __init__(self, flat_amount):
        self.flat_amount = flat_amount


class DiscountTypeBOGO(DiscountTypeBase):
    def __init__(self):
        pass


class DiscountTypeNone(DiscountTypeBase):
    def __init__(self):
        pass


@singledispatch
def calculate_discount(discount_type, item):
    return 0


@calculate_discount.register(DiscountTypePercent)
def _(discount_type: DiscountTypePercent, item):
    return item["price"] * discount_type.percent / 100


@calculate_discount.register(DiscountTypeFlat)
def _(discount_type: DiscountTypeFlat, item):
    return discount_type.flat_amount


@calculate_discount.register(DiscountTypeBOGO)
def _(discount_type: DiscountTypeBOGO, item):
    return item["price"] * (item["quantity"] // 2)


@calculate_discount.register(DiscountTypeNone)
def _(discount_type: DiscountTypeNone, item):
    return 0


@singledispatch
def make_discount_description(discount_type, item):
    return "No discount applied"


@make_discount_description.register(DiscountTypePercent)
def _(discount_type: DiscountTypePercent, item):
    return f"{discount_type.percent}% off"


@make_discount_description.register(DiscountTypeFlat)
def _(discount_type: DiscountTypeFlat, item):
    return f"${discount_type.flat_amount} off"


@make_discount_description.register(DiscountTypeBOGO)
def _(discount_type: DiscountTypeBOGO, item):
    return "Buy one get one free"


@make_discount_description.register(DiscountTypeNone)
def _(discount_type: DiscountTypeNone, item):
    return "No discount applied"


if __name__ == "__main__":
    main()
