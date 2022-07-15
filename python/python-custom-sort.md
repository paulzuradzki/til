# Problem

You want to sort a collection using a custom or logical ordering that is not in alphabetical order. 

# Solution
* Pass a function to the `key` parameter that returns the correct ordering. 
* E.g., below, choices.index('Medium') will return an 1 (where 'Low' is index 0, 'High' is index 2).

```python
import random

choices = ['Low', 'Medium', 'High']
random.seed(2022)
levels = [random.choice(choices) for _ in range(20)]

# alphabetical sort ("H" before "L", "L" before "M")
print(sorted(levels))

# custom order sort (Low, Medium, High)
print(sorted(levels, key=lambda level: choices.index(level)))
```

Output
```
['High', 'High', 'High', 'High', 'High', 'High', 'High', 'High', 'High', 'High', 'Low', 'Low', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium']
['Low', 'Low', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'High', 'High', 'High', 'High', 'High', 'High', 'High', 'High', 'High', 'High']
```
