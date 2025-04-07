# Strategy pattern + OOP polymorphism
# Since we inject the discount type into the item, this is the Strategy pattern.
# Since we have subclasses of the discount type implementing the same interface, this is polymorphism.

from pprint import pprint
from abc import ABC, abstractmethod
from dataclasses import dataclass


def main():
    item = Item(
        name="item1",
        price=300,
        quantity=2,
        # discount_type=BOGODiscount(),
        discount_type=PercentDiscount(10),
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
    discount_type: "DiscountTypeBase"
    discount: float = 0

    def update_discount(self):
        self.discount = self.discount_type.calculate_discount(self)

    def update_discount_description(self):
        self.discount_description = self.discount_type.make_discount_description(self)


class DiscountTypeBase(ABC):

    def __init__(self):
        self.name = "Discount Type"

    @abstractmethod
    def calculate_discount(self, item):
        raise NotImplementedError("Subclasses should implement this method")

    @abstractmethod
    def make_discount_description(self, item):
        raise NotImplementedError("Subclasses should implement this method")

    def __repr__(self):
        return f"{self.__class__.__name__}"


class PercentDiscount(DiscountTypeBase):
    def __init__(self, percent):
        self.percent = percent
        self.name = "Percent Discount"

    def calculate_discount(self, item):
        return item.price * self.percent / 100

    def make_discount_description(self, item):
        return f"{self.percent}% off"


class FlatDiscount(DiscountTypeBase):
    def __init__(self, flat_amount):
        self.flat_amount = flat_amount
        self.name = "Percent Discount"

    def calculate_discount(self, item):
        return self.flat_amount

    def make_discount_description(self, item):
        return f"${self.flat_amount} off"


class BOGODiscount(DiscountTypeBase):
    def __init__(self):
        self.name = "Percent Discount"

    def calculate_discount(self, item):
        return item.price * (item.quantity // 2)

    def make_discount_description(self, item):
        return "Buy one get one free"


class NoDiscount(DiscountTypeBase):
    def __init__(self):
        self.name = "Percent Discount"

    def calculate_discount(self, item):
        return 0

    def make_discount_description(self, item):
        return "No discount applied"


if __name__ == "__main__":
    main()
