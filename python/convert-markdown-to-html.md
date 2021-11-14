# Problem
HTML can be tedious to write or manage.

# Solution
You can start writing in markdown and convert to HTML. Example:

```python
import markdown
from IPython.display import display, HTML

md = """
### Foo Bar
Contact Information

* 123-456-7890
* foo@bar.com
___
## Experience
### Employer 1
Role, Location, Period

* item
* item
* item
* item
___
## Education
### University 1
* Major, GPA
* Notes
"""

# for Jupyter display
# HTML(html)

html = markdown.markdown(md)
print(html)
```

# Output

```
<h3>Foo Bar</h3>
<p>Contact Information</p>
<ul>
<li>123-456-7890</li>
<li>foo@bar.com</li>
</ul>
<hr />
<h2>Experience</h2>
<h3>Employer 1</h3>
<p>Role, Location, Period</p>
<ul>
<li>item</li>
<li>item</li>
<li>item</li>
<li>item</li>
</ul>
<h3>Employer 2</h3>
<p>Role, Location, Period</p>
<ul>
<li>item</li>
<li>item</li>
<li>item</li>
<li>item</li>
</ul>
<hr />
<h2>Education</h2>
<h3>University 1</h3>
<p>Major, GPA
Notes</p>
```
