# Problem

You have deeply nested code that is hard to follow. The "happy path" -- the most common or successful flow -- is not obvious due to being buried within layers of conditions.

# Solution

"Flatten" the code -- that is, reduce nesting & indentation -- to something logically equivalent with the following techniques:
1. Use early returns, aka "guard clauses".
- A guard clause is an early return based on a condition that "guards" the rest of the function. It handles edge cases or invalid inputs immediately, so the main logic can proceed without extra nesting.
- In other words, handle the weird cases early, then proceed with the main logic.
2. If an `if` or `else` branch ends in `return`, `raise`, `break`, or `continue`, you can move the corresponding `else` to the outer level.


Example 1

Before guard clause(s)
```python
def func():
    if cond_1:
        return foo()
    else:
        if cond_2:
            return bar()
        else:
            if cond_3:
                return yow()
            else:
                return woop()
```

After
```python
def func():
    if cond_1:
        return foo()
    if cond_2:
        return bar()
    if cond_3:
        return yow()
    return woop()
```

Example 2

Before
```python
def func():
    if cond_1:
        if cond_2:
            if cond_3:
                return bar()
            else:
                return woop()
        else:
            return foo()
    else:
        return yow()
```

After
```python
def func():
    if not cond_1: 
        return yow()
    if not cond_2: 
        return foo()
    if not cond_3: 
        return woop()
    return bar()
```

Example 3


```python
def func():
    if cond_1:
        if cond_2:
            return foo()
        elif cond_3:
            return bar()
        else:
            return woop()
    else:
        return yow()
```

__

```python
def func():
    if not cond_1:
        return yow()

    # DeMorgan's Law: (~A & ~B) = ~(A | B)
    if not (cond_2 or cond_3):
        return woop()

    if not cond_2:
        return bar()

    return foo()
```


# Discussion

Deeply nested code is hard to follow because the reader has to track more context and possible states within each block of logic. A straight-line procedure reads more naturally.

Guard clauses can make the "happy path" clearer to follow due to 1) less complicated nesting and 2) they often check for the special cases first proceeded by the "happy path". This might be counter-intuitive to put the happy path last; however, it's often preferable to the alternative of hiding it within a bunch of special case handling.

One disadvantage of guard clauses is that they can obscure the importance of conditions which would otherwise be easier to visualize through hierarchical nesting. For example below, there is visual emphasis that the condition `cond_2` is only applicable if `cond_1` is `true`. The first version is arguably clearer.

Without guard clause
```python
def func():
    if cond_1:
        if cond_2:
            return foo()
        else:
            return bar()

    # Unnecessary else
    else:
        return baz()
```

With guard clause

```python
def func():
    if not cond_1:
        return baz()

    if cond_2:
        return foo()

    return bar()
```

<details>
<summary>Test cases</summary>

```python
from unittest.mock import patch

import pytest


# fmt: off
def foo(): return "foo"     
def bar(): return "bar"   
def yow(): return "yow"   
def woop(): return "woop" 
# fmt: on


def func(
    cond_1,
    cond_2,
    cond_3,
):
    if cond_1:
        return foo()
    else:
        if cond_2:
            return bar()
        else:
            if cond_3:
                return yow()
            else:
                return woop()


def func_v2(
    cond_1,
    cond_2,
    cond_3,
):
    if cond_1:
        return foo()
    if cond_2:
        return bar()
    if cond_3:
        return yow()
    return woop()


@pytest.mark.parametrize(
    "cond_1, cond_2, cond_3, expected",
    [
        (True, True, True, "foo"),
        (False, True, True, "bar"),
        (False, False, True, "yow"),
        (False, False, False, "woop"),
    ],
)
def test_func(cond_1, cond_2, cond_3, expected):
    assert func(cond_1, cond_2, cond_3) == expected == func_v2(cond_1, cond_2, cond_3)


@patch("guard.foo", return_value="test foo")
def test_func_mocked_foo_path(mock_foo):
    cond_1, cond_2, cond_3 = True, True, True
    assert func(cond_1, cond_2, cond_3) == mock_foo.return_value
    mock_foo.assert_called_once()
```

</details>