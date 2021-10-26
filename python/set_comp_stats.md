Snippet for quick set comparison statistics.

Python 
```python
import numpy as np

s1 = set([np.random.randint(0,101) for n in range(20)])
s2 = set([np.random.randint(0,101) for n in range(20)])

union = s1|s2
intersection = s1&s2
symmetric_diff = s1^s2
left_diff = s1-s2
right_diff = s2-s1

print("Sets")
print("s1", s1)
print("s2", s2)
print()

print("Set Statistics")
print("len(s1):", len(s1))
print("len(s2):", len(s2))

print("union:",          len(union))
print("intersection:",   len(intersection))
print("symmetric_diff:", len(symmetric_diff))
print("left_diff:",      len(left_diff))
print("right_diff:",     len(right_diff))

n = 5

print()
print("Examples")
print("union:",          np.random.choice(a=list(union), size=n))
print("intersection:",   np.random.choice(a=list(intersection), size=n))
print("symmetric_diff:", np.random.choice(a=list(symmetric_diff), size=n))
print("left_diff:",      np.random.choice(a=list(left_diff), size=n))
print("right_diff:",     np.random.choice(a=list(right_diff), size=n))
```

Output
```
Sets
s1 {3, 4, 6, 18, 23, 24, 44, 54, 55, 56, 57, 59, 60, 67, 73, 79, 80, 85, 86, 89}
s2 {8, 9, 20, 25, 29, 33, 37, 44, 48, 51, 56, 60, 64, 66, 67, 70, 72, 89, 91, 94}

Set Statistics
len(s1): 20
len(s2): 20
union: 35
intersection: 5
symmetric_diff: 30
left_diff: 15
right_diff: 15

Examples
union: [25 48 91 55 37]
intersection: [44 56 67 67 89]
symmetric_diff: [86 86 85 37 29]
left_diff: [55  6 24 59  6]
right_diff: [94 64  9 25  8]
```
