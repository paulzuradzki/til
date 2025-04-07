# Simple conditional

from enum import Enum
from pprint import pprint


def main():
    item = {
        "name": "item1",
        "price": 300,
        "quantity": 2,
    }

    discount_type = DiscountType.BOGO
    discount = calculate_discount(item, discount_type)
    _discount_description = make_discount_description(item, discount_type)

    pprint(
        item
        | {
            "discount_amount": discount,
            "discount_description": _discount_description,
        },
        sort_dicts=False,
    )


class DiscountType(Enum):
    PERCENT = "percentage of total"
    FLAT = "flat amount from total"
    BOGO = "buy one get one free"
    NONE = "no discount applied"


def calculate_discount(item, discount_type):
    if discount_type == DiscountType.PERCENT:
        return item["price"] * item["quantity"] * 0.10
    elif discount_type == DiscountType.FLAT:
        return item["price"] * item["quantity"] - 50
    elif discount_type == DiscountType.BOGO:
        return item["price"]
    else:
        return 0


def make_discount_description(item, discount_type):
    if discount_type == DiscountType.PERCENT:
        return f"10% off on {item['name']}"
    elif discount_type == DiscountType.FLAT:
        return f"Flat $50 off on {item['name']}"
    elif discount_type == DiscountType.BOGO:
        return f"Buy one get one free on {item['name']}"
    else:
        return "No discount applied"


if __name__ == "__main__":
    main()
