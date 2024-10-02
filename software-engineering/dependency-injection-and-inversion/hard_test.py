from unittest.mock import patch


class HardToTest:
    def __init__(self):
        self.dependency = ComplexDependency()

    def do_some_stuff(self):
        print("Doing stuff...")
        print("Doing more stuff...")
        return self.dependency.complicated_method()


class ComplexDependency:
    def __init__(self):
        self.value = 10

    def complicated_method(self):
        return f"Value is {self.value}. Result of complicated method..."


@patch("hard_test.ComplexDependency")
def test_HardToTest_do_some_stuff(mock_complex_dependency, capsys):
    mock_complex_dependency.return_value.complicated_method.return_value = (
        "Mocked result of complicated method..."
    )

    test_object = HardToTest()
    result = test_object.do_some_stuff()
    captured_output = capsys.readouterr()
    assert result == "Mocked result of complicated method..."
    assert captured_output.out == "Doing stuff...\nDoing more stuff...\n"
