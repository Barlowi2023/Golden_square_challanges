import pytest
from lib.return_first_five_words import *

# Test function returns a string
def test_return_five_words_one_string():
    snippet = make_snippet('hello')
    assert snippet == 'hello'

# Test function returns first five words + '...' if more than 5
def test_function_returns_split_words():
    snippet = make_snippet('hello world today is a great day')
    assert snippet == 'hello world today is a ...'




