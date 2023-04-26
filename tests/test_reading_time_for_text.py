import pytest
from lib.reading_time_for_text import *

"""
Given a string of 200 words
It returns the number of seconds 
"""
def test_reading_200_words():
    text = " ".join(["word" for i in range(0, 200)])
    result = reading_time_for_text(text)
    assert result == 1.0

    """
Given a string of 400 words
It returns the number of seconds 
"""
def test_reading_400_words():
    text = " ".join(["word" for i in range(0, 400)])
    result = reading_time_for_text(text)
    assert result == 2.0

"""
Given a string of 300 words
It returns the number of seconds 
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