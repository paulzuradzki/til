`textwrap` is a utility that helps to format text with a specified width, indentation, and other wrap settings (ex: breaking long words, truncation placeholders).
* Sample use case: neatly formatting multiline code comments (ex: SQL, SAS).
* `textwrap` is a module in the Python standard library; there is no additional installation

Example
```python
import textwrap

# configure textwrapper: width of 80 characters, indent of 4 spaces
width = 80
tw = textwrap.TextWrapper(width=width, 
                          initial_indent=' '*4, 
                          subsequent_indent=' '*4)

# process and display text
txt = "The Zen of Python, by Tim Peters\n\nBeautiful is better than ugly.\nExplicit is better than implicit.\nSimple is better than complex.\nComplex is better than complicated.\nFlat is better than nested.\nSparse is better than dense.\nReadability counts.\nSpecial cases aren't special enough to break the rules.\nAlthough practicality beats purity.\nErrors should never pass silently.\nUnless explicitly silenced.\nIn the face of ambiguity, refuse the temptation to guess.\nThere should be one-- and preferably only one --obvious way to do it.\nAlthough that way may not be obvious at first unless you're Dutch.\nNow is better than never.\nAlthough never is often better than *right* now.\nIf the implementation is hard to explain, it's a bad idea.\nIf the implementation is easy to explain, it may be a good idea.\nNamespaces are one honking great idea -- let's do more of those!"
print("\nBEFORE:\n")
print(txt)

# fill/wrap text
txt = tw.fill(txt)

# add SQL-style borders
txt = "/*{0}\n{1}\n{0}*/".format('*'*(width-2), txt)

print("\nAFTER:\n")
print(txt)
```

Before
```
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

After
```
/*******************************************************************************
    The Zen of Python, by Tim Peters  Beautiful is better than ugly. Explicit is
    better than implicit. Simple is better than complex. Complex is better than
    complicated. Flat is better than nested. Sparse is better than dense.
    Readability counts. Special cases aren't special enough to break the rules.
    Although practicality beats purity. Errors should never pass silently.
    Unless explicitly silenced. In the face of ambiguity, refuse the temptation
    to guess. There should be one-- and preferably only one --obvious way to do
    it. Although that way may not be obvious at first unless you're Dutch. Now
    is better than never. Although never is often better than *right* now. If
    the implementation is hard to explain, it's a bad idea. If the
    implementation is easy to explain, it may be a good idea. Namespaces are one
    honking great idea -- let's do more of those!
*******************************************************************************/
```
