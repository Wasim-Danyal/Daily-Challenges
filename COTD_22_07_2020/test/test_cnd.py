import pytest
from usefrom import cotd



def test_one():
    todoo = "word","here","eeee","zed"
    isinstance(cotd.challenge(todoo), str)
    return True

def test_two():
    todoo = "word","here","eeee","zed"
    isinstance(cotd.challenge(todoo), int)
    return False

def test_three():
    todoo = "word","here","eeee","zed"
    isinstance(cotd.challenge(todoo), dict)
    return False