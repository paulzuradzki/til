# Code
```python
# hierarchical configuration files
configs = {'defaults': {'greeting': 'hello', 'subject': 'world', 'punctuation': '!'},
           'child 1': {'subject': 'Paul'},
           'child 2': {'greeting': 'yo yo'}
          }

configs['defaults'], configs['child 1'], configs['child 2']
defaults, attribute1, attribute2 = configs['defaults'], configs['child 1'], configs['child 2']

# config now contains subject from attribute1 (overrode default from 'world' to 'Paul) 
  # and config contains greeting from attribute2 (overrode default from 'hello' to 'yo yo'
  # punctuation is '!' by default and is not overridden by any of the "child" dicts

config = {**defaults, **attribute1, **attribute2}
print(config)
# output: {'greeting': 'yo yo', 'subject': 'Paul', 'punctuation': '!'}
```
