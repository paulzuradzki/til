### Method Chaining

When you write a method that does not have a return value of its own, consider having the method return `self`. If you do this consistently throughout your API, you will enable a style of programming known as method chaining in which an object can be named once and then multiple methods can be invoked on it:
`s2 = s.x(10).y(5).size(50).fill('red')`

```python

class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def x(self, n):
        print(f"called x({n})")
        return self

    def y(self, n):
        print(f"called y({n})")
        return self

    def size(self, n):
        print(f"called size({n})")
        return self

    def fill(self, color):
        print(f"called fill({color})")
        return self
    
    def __repr__(self):
        return f"Square(side_length={self.side_length})"

if __name__ == "__main__":
    s = Square(4)
    s2 = s.x(10).y(5).size(50).fill('red')
    print( id(s) == id(s2) )
```

Output
```
called x(10)
called y(5)
called size(50)
called fill(red)
True
```
