# Software Testing with Pytest Using Mocks and Fixtures

# Problem(s)
1) We want to test the behavior of a function that relies on some other unknown or dynamic thing (e.g., a user's home directory).
2) We will set up a test double resource (a "fixture") that we want to re-use.
3) We want to test the result of side effects for functions with no return value like a print operation to standard output.

We will test 2 functions `get_home_dir` and `print_home_dir`.
* `get_home_dir` returns a string. E.g., 'Users/pzuradzki` on my machine.
* `print_home_dir` prints that value.
                                                                  
# Solution
         
* `Path.home()` is user-specific. We will inject behavior into the `Path` class `home()` method call through mocking.
  * This can be done using a context manager or decorator.
* Since we need to mock `Path` twice, we can also create a fixture for code re-use. See Example #2.
* For `print_home_dir` - we want to capture standard output. `pytest` has a built-in fixture `capsys` that we can use for this.
* In Example #3, we just show another variation of using unittest.mock.patch with a decorator.
* `autospec=True` - it's generally good to use `autospec=True` by default. `autospec=True` makes your mock match the specification of class attributes and methods of the class being mocked. Otherwise, your mock class may accept invalid methods. This leaves your test being susceptible to bugs like typos in method calls. These invalid method calls could pass your tests inadvertently.

# References
* https://docs.python.org/3/library/unittest.mock.html#
* https://docs.pytest.org/en/7.4.x/contents.html

# Terms
* `fixture`
    * In unittest, you typically use setUp and tearDown methods to set up a fixed environment ("fixture") for each test case to run in.
    * In pytest, fixtures are more flexible and can be created using the `@pytest.fixture` decorator. They are functions that return a resource and can be injected into test functions as arguments.
* `mock` - Mocks are objects that mimic the behavior of real objects in a controlled way. The `unittest` library has a `Mock` class in its `unittest.mock` module for creating mock objects. Mocks can be configured to return specific values when invoked, allowing you to isolate the code under test from external dependencies.
* `monkeypatching` 
    * In `unittest`, Monkey patching generally refers to dynamically modifying or extending the behavior of classes or modules at runtime. In unittest, you might use the unittest.mock library to replace attributes temporarily. Monkeypatching is simpler and more limited in scope compared to mocking. You can set attributes with monkeypatch but you need mocking to mock behavior like return values and side effects.
    * In `pytest`, Pytest makes monkey patching easy with its built-in monkeypatch fixture, which allows you to modify classes, functions, dictionaries, and more.

# Example
___

```python
"""home_dir.py
"""
from pathlib import Path


def get_home_dir() -> str:
    return str(Path.home())


def print_home_dir() -> None:
    print(get_home_dir())


if __name__ == "__main__":
    print_home_dir()
```

___

Test Example #1. Using `patch.object` context managers. Note the repetition in both tests.

```python
"""test_home_dir.py
"""
from pathlib import Path
from unittest.mock import patch

import home_dir


def test_get_home_dir() -> None:
    with patch.object(Path, "home", return_value="test/test"):
        assert home_dir.get_home_dir() == "test/test"


def test_print_home_dir(capsys) -> None:
    with patch.object(Path, "home", return_value="test/test"):
        home_dir.print_home_dir()
        output = capsys.readouterr().out.strip()
        assert output == "test/test"
```

___

Test Example #2. With user-created fixture.

Here we create our own `mocked_path` fixture for re-use on both tests. We pass `mocked_path` as an argument to the test functions (even though they're not called directly in the test functions). The `mocked_path` will override any calls to `Path`.

```python
"""test_home_dir.py
"""
from pathlib import Path
from unittest.mock import patch

import home_dir
import pytest


@pytest.fixture
def mocked_home_path():
    with patch.object(Path, "home", return_value="test/test") as mocked_home_path:
        yield mocked_home_path


def test_get_home_dir(mocked_home_path) -> None:
    assert home_dir.get_home_dir() == "test/test"


def test_print_home_dir(capsys, mocked_home_path) -> None:
    home_dir.print_home_dir()
    output = capsys.readouterr().out.strip()
    assert output == "test/test"

```

Test Example #3a

Using patch decorator.

```python
"""test_home_dir.py
"""
from unittest.mock import patch

import home_dir


@patch("home_dir.Path.home", return_value="test/test")
def test_get_home_dir(mocked_home_path) -> None:
    assert home_dir.get_home_dir() == "test/test"


# patch passes the mock as first argument
# so ordering of ('mocked_home_path, capsys') arguments matter
@patch("home_dir.Path.home", return_value="test/test")
def test_print_home_dir(mocked_home_path, capsys) -> None:
    home_dir.print_home_dir()
    output = capsys.readouterr().out.strip()
    assert output == "test/test"

```

Test Example #3a

Subtle difference: using `@patch.object` instead of `@patch`.
```python
"""test_home_dir.py
"""
from pathlib import Path
from unittest.mock import patch

import home_dir
import pytest


@patch.object(Path, "home", return_value="test/test", autospec=True)
def test_get_home_dir(mocked_home_path) -> None:
    assert home_dir.get_home_dir() == "test/test"


# patch passes the mock as first argument
# so ordering of ('mocked_home_path, capsys') arguments matter
@patch.object(Path, "home", return_value="test/test", autospec=True)
def test_print_home_dir(mocked_home_path, capsys) -> None:
    home_dir.print_home_dir()
    output = capsys.readouterr().out.strip()
    assert output == "test/test"
```
___

# Discussion
* Be cautious not to over-use mocking. 
* Mocks are time-consuming and tend to test implementation rather than behavior. 
* Your tests are more likely to fail in spite of valid code changes (refactoring).
* That being said, they can help a lot to isolate parts of the system that you are testing.
