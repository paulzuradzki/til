from unittest.mock import Mock, patch


class EasierToTest:
    def __init__(self, dependency: "ComplexDependency"):
        self.dependency = dependency

    def do_some_stuff(self):
        print("Doing stuff...")
        print("Doing more stuff...")
        return self.dependency.complicated_method()


class ComplexDependency:
    def __init__(self):
        self.value = 10

    def complicated_method(self):
        return f"Value is {self.value}. Result of complicated method..."


@patch("easier_test.ComplexDependency")
def test_EasierToTest_do_some_stuff(mock_complex_dependency, capsys):
    mock_complex_dependency = Mock()
    test_object = EasierToTest(dependency=mock_complex_dependency)
    _result = test_object.do_some_stuff()
    captured_output = capsys.readouterr()
    assert captured_output.out == "Doing stuff...\nDoing more stuff...\n"

