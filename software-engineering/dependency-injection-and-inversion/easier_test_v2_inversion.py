from abc import ABC, abstractmethod


class EasierToTest:
    def __init__(self, dependency: "DependencyInterface"):
        self.dependency = dependency

    def do_some_stuff(self):
        print("Doing stuff...")
        print("Doing more stuff...")
        return self.dependency.complicated_method()


class DependencyInterface(ABC):
    @abstractmethod
    def complicated_method(self):
        pass


class ComplexDependency(DependencyInterface):
    def __init__(self):
        self.value = 10

    def complicated_method(self):
        return f"Value is {self.value}. Result of complicated method..."


# Derived class for testing
class DerivedComplexDependency(DependencyInterface):
    def __init__(self):
        pass

    def complicated_method(self):
        return "Mocked value is FOO. Mocked result of complicated method..."


def test_EasierToTest_do_some_stuff(capsys):
    test_object = EasierToTest(dependency=DerivedComplexDependency())
    _ = test_object.do_some_stuff()
    captured_output = capsys.readouterr()
    assert captured_output.out == "Doing stuff...\nDoing more stuff...\n"
