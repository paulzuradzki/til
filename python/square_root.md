### Algorithm to determine the square root of N:
* start with an arbitray guess (ex: 1)
* square the guess and take the absolute value of the difference from N
  * if it's close enough within some tolerance value (ex: 0.0001), then return the guess
  * else, make a new guess equal to the average of (guess + N/guess) and re-attempt

```python

def square_root(n):
    def good_enough(guess, n):
        tolerance = 0.0001
        is_it_good_enough = abs(guess**2 - n) <= tolerance
        return is_it_good_enough

    def attempt(guess=None, n=None):
        if good_enough(guess, n):
            return guess
        else:
            return attempt((guess + n/guess)/2, n)

    return attempt(guess=1, n=n)

def square_root_with_prints(n):
    def good_enough(guess, n):
        tolerance = 0.0001
        is_it_good_enough = abs(guess**2 - n) <= tolerance
        print(f"is_it_good_enough: {is_it_good_enough}")
        return is_it_good_enough

    def attempt(guess=None, n=None):
        print(f"guess: {guess}")
        if good_enough(guess, n):
            return guess
        else:
            print(f"new guess: ({guess} + {n} / {guess}) / 2")
            return attempt((guess + n/guess)/2, n)

    return attempt(guess=1, n=n)

```

```
>>> square_root(10)
3.162277665175675

>>> square_root_with_prints(10)`
guess: 1
is_it_good_enough: False
new guess: (1 + 10 / 1) / 2
guess: 5.5
is_it_good_enough: False
new guess: (5.5 + 10 / 5.5) / 2
guess: 3.659090909090909
is_it_good_enough: False
new guess: (3.659090909090909 + 10 / 3.659090909090909) / 2
guess: 3.196005081874647
is_it_good_enough: False
new guess: (3.196005081874647 + 10 / 3.196005081874647) / 2
guess: 3.16245562280389
is_it_good_enough: False
new guess: (3.16245562280389 + 10 / 3.16245562280389) / 2
guess: 3.162277665175675
is_it_good_enough: True
```
