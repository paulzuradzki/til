# Problem

You want to sort a collection using a custom or logical ordering that is not in alphabetical order. 

# Solution
* Pass a function to the `key` parameter that returns the correct ordering. 
* E.g., below, choices.index('Medium') will return an 1 (where 'Low' is index 0, 'High' is index 2).

```python
sort_order = ['Low', 'Medium', 'High']
data = ['High', 'Medium', 'Medium', 'High', 'Medium', 'Low']

sorted(data, key=lambda value: sort_order.index(value))
# => ['Low', 'Medium', 'Medium', 'Medium', 'High', 'High']
```

# Resources

[Reuven Lerner - How to sort anything](https://www.youtube.com/watch?v=Z3c2LvEJeu0)
* covers use of operator.itemgetter()
* OOP gt/lt methods
* dataclasses with order=True and order of attribute inits
