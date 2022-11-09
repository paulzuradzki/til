
Demonstration of formatting log output and re-directing to a file using basic configuration. 
* To support multiple outputs, see docs on how to create multiple loggging "handler" objects.
* Also check out configuring from a dictionary.

Code
```python
# hello.py
import logging
from pathlib import Path
from datetime import datetime

dt = datetime.now().strftime('%Y%m%d-%H%M%S')
module_name = Path(__file__).name.replace('.py', '')
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(process)d - %(levelname)s - %(message)s',
    filename=f'.logs/{dt}_{module_name}.log'
)

logging.info("hello from hello.py")
```

Output
```
# .logs/20221109-101152_hello.log
2022-11-09 10:11:52,926 - 53193 - INFO - hello from hello.py
```


Resources on logging
* https://docs.python.org/3/howto/logging.html#
* https://realpython.com/python-logging/
* https://realpython.com/python-logging-source-code/
* https://python-patterns.guide/gang-of-four/composition-over-inheritance/
