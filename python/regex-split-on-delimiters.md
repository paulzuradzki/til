# Problem

I have a list of delimiters on which I want to split a string. 
* These delimiters often include characters that must be escaped.
* I want a clean way to separate each escaped delimiter with a `|` (pipe; logical "or").

This is handy for standardizing and tokenizing text.

# Solution

Tools: `re.escape()` and `re.split()`

```python
import re

delimiters = list(';?_/.* ')
pattern = re.compile(r'|'.join(map(re.escape, delimiters)))

line = "The cat in the hat; the dog on the mat? **wow* hello_world"
tokens = [token.lower() 
          for token in pattern.split(line) 
          if token]

print(pattern)      # re.compile('\\;|\\?|_|\\/|\\.|\\*|\\ ')
print(tokens)       # ['the', 'cat', 'in', 'the', 'hat', 'the', 'dog', 'on', 'the', 'mat', 'wow', 'hello', 'world']
```
