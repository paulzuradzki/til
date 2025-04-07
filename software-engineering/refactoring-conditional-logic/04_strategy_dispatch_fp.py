# Strategy pattern with functions instead of polymorphism
# Behavior is selected at runtime and delegated to an interchangeable, encapsulated unit of logic (in this case, a function).
# AKA, functional dispatching

from pprint import pprint


def main():
    item = {
        "name": "item1",
        "price": 300,
        "quantity": 2,
    }

    discount_type = "bogo"
    discount_func = get_discount_calculator(discount_type)
    discount = discount_func(item)
    discount_description = make_discount_description(item, discount_type)

    pprint(
        item
        | {
            "discount_amount": discount,
            "discount_description": discount_description,
        },
        sort_dicts=False,
    )


def get_discount_calculator(discount_type):
    return {
        "percent": calculate_percent_discount,
        "flat": calculate_flat_discount,
        "bogo": calculate_bogo_discount,
        "none": calculate_no_discount,
    }.get(discount_type, calculate_no_discount)


def calculate_percent_discount(item):
    return item["price"] * 0.10


def calculate_flat_discount(item):
    return item["price"] - 50


def calculate_bogo_discount(item):
    return item["price"] * (item["quantity"] // 2)


def calculate_no_discount(item):
    return 0


def make_discount_description(item, discount_type):
    return {
        "percent": make_discount_description_percent,
        "flat": make_discount_description_flat,
        "bogo": make_discount_description_bogo,
        "none": make_discount_description_none,
    }.get(discount_type, make_discount_description_none)(item)


def make_discount_description_percent(item):
    return f"10% off on {item['name']}"


def make_discount_description_flat(item):
    return f"Flat $50 off on {item['name']}"


def make_discount_description_bogo(item):
    return f"Buy one get one free on {item['name']}"


def make_discount_description_none(item):
    return "No discount applied"


if __name__ == "__main__":
    main()
