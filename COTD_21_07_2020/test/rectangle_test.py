import pytest
from code.abcrectangle import area


def test_one():
    assert (type(area(3,6)) == int)
    return True