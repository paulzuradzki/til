# Problem

I want to show code diffs in markdown or GitHub comments.

# Solution

Use code fence block (` ``` `) with `diff` and `+`/`-` symbol for additions and deletions.

````
```diff
- def hello():
-    print("hello")

+ def HELLO():
+     print("WHY ARE WE YELLING!")
```
````

Renders to

```diff
- def hello():
-    print("hello")

+ def HELLO():
+     print("WHY ARE WE YELLING!")
```