import pytest
from challenge.stringgen import string_gen

def test_one():
    assert len(string_gen()) == 5

def test_two():
    assert type(string_gen()) == str

def test_three():
    assert type(string_gen()) != list, float

def test_four():
    assert type(string_gen()) != int
