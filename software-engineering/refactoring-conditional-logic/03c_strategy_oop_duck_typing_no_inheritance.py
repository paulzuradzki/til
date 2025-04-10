# Strategy pattern with OOP - no inheritance

from pprint import pprint
from typing import Protocol
from dataclasses import dataclass


def main():
    item = Item(
        name="item1",
        price=300,
        quantity=2,
        discount_type=BOGODiscountStrategy(),
        # discount_type=PercentDiscountStrategy(10),
    )

    item.update_discount()
    item.update_discount_description()

    pprint(
        item.__dict__,
        sort_dicts=False,
    )


@dataclass
class Item:
    name: str
    price: float
    quantity: int
    discount_type: "DiscountStrategy"
    discount: float = 0

    def update_discount(self):
        self.discount = self.discount_type.calculate_discount(self)

    def update_discount_description(self):
        self.discount_description = self.discount_type.make_discount_description(self)

class DiscountStrategy(Protocol):
    def calculate_discount(self, item: Item) -> float:
        pass

    def make_discount_description(self, item: Item) -> str:
        pass

    def __repr__(self):
        pass

@dataclass
class PercentDiscountStrategy:
    percent: float
    name: str = "Percent Discount"

    def calculate_discount(self, item):
        return item.price * self.percent / 100

    def make_discount_description(self, item):
        return f"{self.percent}% off"    

@dataclass
class FlatDiscountStrategy:
    flat_amount: float
    name: str = "Flat Discount"

    def calculate_discount(self, item):
        return self.flat_amount

    def make_discount_description(self, item):
        return f"${self.flat_amount} off"

@dataclass
class BOGODiscountStrategy:
    name: str = "BOGO Discount"
    
    def calculate_discount(self, item):
        return item.price * (item.quantity // 2)

    def make_discount_description(self, item):
        return "Buy one get one free"

@dataclass
class NoDiscountStrategy:
    name: str = "No Discount"

    def calculate_discount(self, item):
        return 0

    def make_discount_description(self, item):
        return "No discount applied"


if __name__ == "__main__":
    main()
