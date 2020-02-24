# pylint: disable=invalid-name,missing-module-docstring,missing-function-docstring
import vtpy
import pprint


def check_positive_plan(result):
    assert "VPSPLANID" in result
    assert "name" in result
    assert "plan_type" in result
    #    print(type(result))
    return


def test_api():
    result = vtpy.planlist()
    x = list(result.keys())[0]
    check_positive_plan(result[x])
