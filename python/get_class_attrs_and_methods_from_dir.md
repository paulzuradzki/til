# Problem
* I want to list all class attributes and methods separately without dunder methods. 
* The `dir()` command outputs all attributes, methods, and dunder methods together.

# Solution

Use a list comprehesnion to filter out dunder methdods and separate attributes from methods using Python built-in `callable()` function.

```python
class Point:
    """A point in 2D space; a.k.a., a Cartesian x-y coordinate."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"


point = Point(3, 4)

class_attrs = [
    attr
    for attr in dir(point)
    if not attr.startswith("__") and not callable(getattr(point, attr))
]
class_methods = [
    attr
    for attr in dir(point)
    if not attr.startswith("__") and callable(getattr(point, attr))
]

print(point, end="\n\n")
print(f"Class attributes:\n{class_attrs}")
print()
print(f"Class methods:\n{class_methods}")
```

# Output

```
Point(3, 4)

Class attributes:
['x', 'y']

Class methods:
['distance']
```
