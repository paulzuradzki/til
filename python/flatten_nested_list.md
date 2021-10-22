### Using generators to recursively iterate through nested iterables

Source: "Python Distilled" by David Beazley

```python

# Using yield
def flatten(items):
    for i in items:
        if isinstance(i, list):
            for j in flatten(i):
                yield j
        else:
            yield i

# Using `yield from` to delegate iteration to outer iteration; otherwise, same as above
def flatten(items):
    for i in items:
        if isinstance(i, list):
            yield from flatten(i)            
        else:
            yield i

# Works around recursion limit
  # Puts data on an internal list as opposed to 
  # building frames on the internal interpreter stack.
  # stack has 1 iterable on first iteration, so next() gets first value in `items`
  # we keep appending iterables to the stack; next() will return latest iterable

def flatten_w_stack(items):
    stack = [ iter(items) ]
    while stack:
        try:
            item = next(stack[-1])
            if isinstance(item, list):
                stack.append(iter(item))
            else:
                yield item
        except StopIteration:
            stack.pop()

if __name__ == "__main__":
    nested = [1, 2, [3, [4, 5], 6, 7], 8]
    flat = [x for x in flatten(nested)]             # => [1, 2, 3, 4, 5, 6, 7, 8]
    flat2 = [x for x in flatten_w_stack(nested)]
