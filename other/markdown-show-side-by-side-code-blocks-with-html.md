# How To: Show code blocks side-by-side in markdown with html

<div style="display: flex; gap: 1rem;">

<div style="flex: 1;">

```python
# Code block 1
def greet():
    print("Hello, world!")

```
</div>

<div style="flex: 1;">

```javascript
// Code block 2
function greet() {
console.log("Hello, world!");
}
```

</div>

</div>

___

Escaped

````markdown
<div style="display: flex; gap: 1rem;">

<div style="flex: 1;">

```python
# Code block 1
def greet():
    print("Hello, world!")

```
</div>

<div style="flex: 1;">

```javascript
// Code block 2
function greet() {
console.log("Hello, world!");
}
```

</div>

</div> <!-- close flex container to start showing things below -->
````

# On GitHub

GitHub markdown is more strict and strips out styles, so the approach above won't work in GitHub.
