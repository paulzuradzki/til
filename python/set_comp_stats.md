Snippet for quick set comparison statistics.

Python 
```python
s1 = {1, 2, 5, 6, 8, 10, 11, 13, 14, 16, 17}
s2 = {0, 1, 5, 7, 8, 9, 10, 12, 13, 14, 15, 17, 18, 19}
union = s1|s2
intersection = s1&s2
symmetric_diff = s1^s2
left_diff = s1-s2
right_diff = s2-s1

print('Set Statistics')
print("union:",          len(union))
print("intersection:",   len(intersection))
print("symmetric_diff:", len(symmetric_diff))
print("left_diff:",      len(left_diff))
print("right_diff:",     len(right_diff))

print()
print('Examples')
print("union:",          list(union)[:5])
print("intersection:",   list(intersection)[:5])
print("symmetric_diff:", list(symmetric_diff)[:5])
print("left_diff:",      list(left_diff)[:5])
print("right_diff:",     list(right_diff)[:5])
```

Output
```
Set Statistics
union: 18
intersection: 7
symmetric_diff: 11
left_diff: 4
right_diff: 7

Examples
union: [0, 1, 2, 5, 6]
intersection: [1, 5, 8, 10, 13]
symmetric_diff: [0, 2, 6, 7, 9]
left_diff: [16, 2, 11, 6]
right_diff: [0, 7, 9, 12, 15]
```
