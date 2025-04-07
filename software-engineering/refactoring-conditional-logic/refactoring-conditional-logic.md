# Refactoring Conditional Logic

# Problem

You have have a lot of branching logic based on some notion of type. 

```python
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
```

For example,
- Multiple discount types for pricing: "percent discount", "no discount", "buy one, get one discount". Based on the discount type, you might have different calculation logic or display text logic.
- Role types like SuperUser, StaffUser, RegisteredUser, and PublicUser to control authorization on an application.

If multiple behaviors rely on these checks (e.g., pricing, logging, display), your code will be littered with similar `if/elif` or `isinstance()` checks. This violates the Open/Closed principle: code should be open to extension but closed to modification. Adding a new type will require changes in multiple places. This is due to coupling between the conditional checks and behavior.

# Solution

Try any of examples #2-5 below and compare to using a simple conditional (example #1).

Compare
1. [01_simple_conditional.py](./01_simple_conditional.py) - Simple conditional
2. [02_oop_polym.py](./02_oop_polym.py) - **OOP polymorphism**. Use a common interface (e.g., DiscountType) and subclass per behavior, each overriding a method like .calculate_discount().
3. [03_strategy_oop_polym.py](./03_strategy_oop_polym.py) - **Strategy pattern with polymorphism**. Inject a strategy object (e.g., discount_strategy) into the context (Item). The strategy object encapsulates behavior and adheres to a shared interface. 
4. [04_strategy_dispatch_fp.py](./04_strategy_dispatch_fp.py) - **Strategy pattern with functions, AKA, functional dispatch**. Pass behavior as first-class functions or select them dynamically via a dispatch dictionary. Each function encapsulates one strategy.
5. [05_singledispatch.py](./05_singledispatch.py) - **functools.singledispatch**. Use Python’s dynamic dispatch system to route behavior based on the type of the first argument

# Discussion

Using one of the alternative strategies to if-else might introduce too much indirection or boilerplate. For simple or stable domains, this can be over-engineering. If you're (1) reasonably confident that you need to support more subtypes or specialized behaviors and/or (2) you find yourself repeating the same conditional checks in multiple places, then refactoring to one of the other techniques above might be worthwile. Start with a simple `if` or ` match-case` statement if branching is small or stable. 

The strategy pattern with functions is a nice choice for lightweight extensibility. By extracting inline code from each conditon into a function, you also get smaller, easier-to-test units.
