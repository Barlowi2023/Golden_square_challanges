from lib.greet import *

def test_greet1():
    result = greet("Dave")
    assert result == "Hello, Dave!"

# def test_greet2():
#     result = greet("Bob")
#     assert result == f"Hello, Bob!"