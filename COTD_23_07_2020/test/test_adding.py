import pytest 
from program import adding

def test_one():
    input = str(9)
    isinstance(adding.adder(input), int)
    return True