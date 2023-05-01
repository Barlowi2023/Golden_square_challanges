
{{PROBLEM}} Function Design Recipe

1. Describe the Problem
Put or write the user story here. Add any clarifying notes you might have.

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

2. Design the Function Signature
Include the name of the function, its parameters, return value, and side effects.

# EXAMPLE

def reading_time_for_text(str):
    """shows estimate for reading time from text assuming one reads 200 words per minute

    Parameters: (list all parameters and their types)
        str: a string containing words (e.g. "hello WORLD")

    Returns: (state the return value and its type)
        a float (e.g. 1.0)

    Side effects: (state any side effects)
        This function only works with strings
    """
    pass # Test-driving means _not_ writing any code here yet.

3. Create Examples as Tests
Make a list of examples of what the function will take and return.

# EXAMPLE

"""
Given a string of 200 words
It returns the number of minutes 
"""
reading_time_for_text("... 200 words ...") => 1.0

"""
Given a string of 400 words
It returns the number of seconds 
"""
reading_time_for_text("... 400 words ...") => 2.0

"""
Given a string of 200 words
It returns the number of seconds 
"""
reading_time_for_text("... 300 words ...") => 1.5


"""
Given an empty string
It returns an exception message
"""
reading_time_for_text("") => "PLease enter a longer string"




4. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.


import pytest
from lib.reading_time_for_text import *


"""
Given a string of 200 words
It returns the number of minutes as a float 
"""
def test_reading_200_words():
    text = " ".join(["word" for i in range(0, 200)])
    result = reading_time_for_text(text)
    assert result == 1.0

"""
Given a string of 400 words
It returns the number of minutes as a float 
"""
def test_reading_400_words():
    text = " ".join(["word" for i in range(0, 400)])
    result = reading_time_for_text(text)
    assert result == 2.0

"""
Given a string of 300 words
It returns the number of minutes as a float 
"""
def test_reading_300_words():
    text = " ".join(["word" for i in range(0, 300)])
    result = reading_time_for_text(text)
    assert result == 1.5

"""
Given an empty string
It returns a message
"""
def test_empty_string():
    with pytest.raises(Exception) as e:
        result = reading_time_for_text('')
    error_message = str(e.value)
    assert error_message == "PLease enter a longer string"

Ensure all test function names are unique, otherwise pytest will ignore them!