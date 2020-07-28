import pytest
from program import usefrom

def test_one():
    assert(usefrom.name("I am in Amsterdam am I?") == 2)
    return True

def test_two():
    isinstance(usefrom.name("I am in Amsterdam am I?"), str)