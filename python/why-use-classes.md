### Why use classes?
1. Enable you to group related data structures and functions
    * helps make the code mirror the problem / domain
    * which helps to manage complexity and reason about the problem
2. Encourage code reuse and extensibility, e.g., extending other classes via inheritance
3. Metaprograming - we can customize class instantiation, e.g., via rules and error-checking

### When should I use classes?
When you find yourself re-using shared data between logically related functions, classes might simplify your code. 
* For example, below, we are passing the same configuration around to related functions. We can make this config accessible to other procedures while controlling its namespace.
   * Using classes soley for a namespace is sometimes considered an antipattern in Python. Consider modules (.py file) and a simple data structures if a namespace is all you need.
* What if we were passing around a data structure where we modify its state? A purely functional style can lead to unnecessary re-computation or awkard nested calls, we must read the code from right to left. 
   * E.g., `do_foo(do_bar(do_yow(config)))`.
   * For a more functional style, we might even consider piping operations using ["chained methods"](https://github.com/paulzuradzki/til/blob/master/python/method-chaining.md) 
* Citation: [In Praise of Metaclasses! by David Beazely via `USENIX ;login: series`](https://www.usenix.org/publications/login/winter2016/beazley)

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
