# Problem
I want to pretty-print a collection of elements. The left- and right-hand side should be neatly aligned and separated for readability.

# Solution
* Print formatted output with padding and custom padding character using f-string and format specifiers.
  * Below, `:.<50`, says to left align the string and pad up to 50 characters with a `.` (dot). 
  * The effect is to create neatly aligned separation.
* or use `tabulate` package

# References
https://pyformat.info/

# Example - with f-string and format specifier

```python
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for idx, letter in enumerate(alphabet):
    print(f"{idx:.<50} {letter}")
```

Output
```
0................................................. A
1................................................. B
2................................................. C
3................................................. D
4................................................. E
5................................................. F
6................................................. G
7................................................. H
8................................................. I
9................................................. J
10................................................ K
11................................................ L
12................................................ M
13................................................ N
14................................................ O
15................................................ P
16................................................ Q
17................................................ R
18................................................ S
19................................................ T
20................................................ U
21................................................ V
22................................................ W
23................................................ X
24................................................ Y
25................................................ Z
```

# Example - using `tabulate` package

```python
from tabulate import tabulate
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(tabulate(enumerate(alphabet)))
```

```
--  -
 0  A
 1  B
 2  C
 3  D
 4  E
 5  F
 6  G
 7  H
 8  I
 9  J
10  K
11  L
12  M
13  N
14  O
15  P
16  Q
17  R
18  S
19  T
20  U
21  V
22  W
23  X
24  Y
25  Z
--  -
```
