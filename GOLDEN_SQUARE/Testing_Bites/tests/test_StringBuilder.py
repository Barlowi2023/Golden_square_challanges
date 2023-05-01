from lib.StringBuilder import *

#Test the initial class returns and empty string 
def test_StringBuilder_1():
    string = StringBuilder()
    assert string.output() == ''

#Test multiple string size
def test_StringBuilder_2():
    string = StringBuilder()
    string.add("hello")
    string.add(" ")
    string.add("world")
    assert string.size() == 11

#Test multiple strings output
def test_StringBuilder_3():
    string = StringBuilder()
    string.add("hello")
    string.add(" ")
    string.add("world")
    assert string.output() == "hello world"





    
    # result1 = string.output()
    # assert result1 == "hello"






# def test_StringBuilder2():
#     string = StringBuilder()
#     actual_string = string.add("hello")
#     result = string.output()
#     assert result == "hello"