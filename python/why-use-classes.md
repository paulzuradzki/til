### Why use classes?
1. Group related data structures and functions
    * this also helps make the code mirror the problem / domain
    * which helps to manage complexity and reason about the problem
2. Code reuse and extensibility, e.g., extending other classes via inheritance
3. Metaprograming - customize class instantiation, e.g., via rules and error-checking

### When should I use classes?
When you find yourself re-using shared data between logically related functions, classes might simplify your code.

Citation:
[In Praise of Metaclasses! by David Beazely via `USENIX ;login: series`](https://www.usenix.org/publications/login/winter2016/beazley)

```
# passing config looks a bit repetitive
config = {...}
do_foo(config, params1)
do_bar(config, params2)
do_yow(config, params3)

# maybe this usage would be less redundant?
td = ThingDoer(config)  # initialize class
td.do_foo(params1)      # call methods (functions in classes) that have access to the attribute 'config'
td.do_bar(params2)
td.do_yow(params3)

```

Without classes
```python
# Object-Oriented Programming Demo
# Use case 1: collect data structures and functions into logical objects

point = {'x': 1, 'y': 2}

def move(point, dx, dy):
    point['x'] += dx
    point['y'] += dy

def display(point):
    print(f"Point(x={point['x']}, y={point['y']})")

# usage
move(point, 2, 2)
print(point)        # {'x': 2, 'y': 4}
display(point)      # Point(x=2, y=4)
```

With classes
* it's explicit that these attributes and functions/methods are related
* the `x` and `y` attributes are not passed to each method redundantly, since this data is implicilty available through the object itself
```python

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def display(self):
        print(self)
    
    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

# usage
p = Point(x=1, y=2)
print(p)                # Point(x=1, y=2)
p.move(2,2)
p.display()             # Point(x=3, y=4)
```
