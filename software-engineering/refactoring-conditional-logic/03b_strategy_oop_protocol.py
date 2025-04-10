# Using protocol instead of inheritance

from pprint import pprint
from dataclasses import dataclass
from typing import Protocol


def main():
    item_data = {
        "name": "item1",
        "price": 300,
        "quantity": 2,
    }

    item = Item(**item_data)
    # discount = DiscountTypePercent(10)
    discount: DiscountTypeProtocol = DiscountTypeBOGO()
    discount_amount = discount.calculate_discount(item)
    discount_description = discount.make_discount_description(item)
    discount_type = discount

    pprint(
        item.__dict__
        | {
            "discount_amount": discount_amount,
            "discount_description": discount_description,
            "discount_type": discount_type,
        },
        sort_dicts=False,
    )


class DiscountTypeProtocol(Protocol):
    def calculate_discount(self, item: "Item") -> float:
        ...

    def make_discount_description(self, item: "Item") -> str:
        ...


@dataclass
class Item:
    name: str
    price: float
    quantity: int


class DiscountTypePercent:
    def __init__(self, percent):
        self.percent = percent

    def calculate_discount(self, item):
        return item.price * self.percent / 100

    def make_discount_description(self, item):
        return f"{self.percent}% off"


class DiscountTypeBOGO:
    def calculate_discount(self, item):
        return item.price * (item.quantity // 2)

    def make_discount_description(self, item):
        return "Buy one get one free"


class DiscountTypeFlat:
    def __init__(self, amount):
        self.amount = amount

    def calculate_discount(self, item):
        return item.price - self.amount

    def make_discount_description(self, item):
        return f"Flat ${self.amount} off"


class DiscountTypeNone:
    def calculate_discount(self, item):
        return 0

    def make_discount_description(self, item):
        return "No discount applied"


if __name__ == "__main__":
    main()
