# pylint: disable=invalid-name,missing-module-docstring,missing-function-docstring
def func(x):
    return x + 1


def test_answer():
    assert func(3) == 4
