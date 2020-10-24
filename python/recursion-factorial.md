Notes
* Many texts demonstrate the factorial function using a loop and using a recursive function call of n*(n-1). 
* The less obvious method is the "iterative process" that still uses recursion. 
  * This method is described in the Structure and Interpretation of Computer Programs (SICP).
  * See factorial_iter()
  * Do not confuse the notion of a recursive process vs a recursive prodedure (function)
  * The iterative process can be picked up at any intermediate step, since state is tracked
  * Not so with the recursive process. The interpreter must keep track of deferred operations
  * A language that implements tail-call recursion will allow an iterative process to grow in constance space
  * Languages without this feature can exceed recursion depth due to the recursive function call, despite the process being iterative

```python
"""factorial.py

3 ways to compute a factorial(n):
* Iterative process with recursive function call and running product
* Linear recursive process
* Iterative process using a loop and running product

Reference:
    https://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book-Z-H-11.html#%_sec_1.2.1
"""

def factorial_iter(n):
    """Iterative process with running product.
    
        Note that this is still a recursive function call. 
        In SICP, we still call this iterative.
    """
    def _factorial_iter(product, counter, max_count):
        if counter > max_count:
            return product
        else:
            return _factorial_iter(counter*product, counter + 1, max_count)
    
    return _factorial_iter(1, 1, n)

def factorial_recur(n):
    """Linear recursive process."""
    if n <= 1:
        return 1
    else:
        return n * factorial_recur(n-1)

def factorial_loop(n):
    """Iterative approach with a loop and running product."""
    product = 1
    counter = n # don't need separate counter var, but this is explicit
    while counter > 1:
        product = product * counter
        counter -= 1
    return product

print("iterative recursive")
for n in range(6):
    print(f'{n}! -> {factorial_iter(n)}')

print("linear recursive")
for n in range(6):
    print(f'{n}! -> {factorial_recur(n)}')

print("iterative with loop")
for n in range(6):
    print(f'{n}! -> {factorial_loop(n)}')
```

### Output

```
>>> python factorial.py
iterative recursive
0! -> 1
1! -> 1
2! -> 2
3! -> 6
4! -> 24
5! -> 120
linear recursive
0! -> 1
1! -> 1
2! -> 2
3! -> 6
4! -> 24
5! -> 120
iterative with loop
0! -> 1
1! -> 1
2! -> 2
3! -> 6
4! -> 24
5! -> 120
```
