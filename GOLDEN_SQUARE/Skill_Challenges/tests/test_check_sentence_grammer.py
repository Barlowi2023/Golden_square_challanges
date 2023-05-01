import pytest
from lib.check_sentence_grammer import *

"""
Given a valid senetence with a capital letter and a full stop
It returns True
"""
def test_with_capital_letter_and_full_stop():
    result = check_sentence_grammer("Hello this is a nice day.")
    assert result == True

"""
Given a valid senetence with a capital letter and a question mark
It returns True
"""
def test_with_capital_letter_and_question_mark():
    result = check_sentence_grammer("Hello this is a nice day?")
    assert result == True

"""
Given an invalid sentence with a capital letter and no full stop
It returns False
"""
def test_with_no_capital_letter_and_full_stop():
    result = check_sentence_grammer("hello this is a nice day.")
    assert result == False

"""
Given an invalid sentence with no capital letter and a full stop
It returns False
"""
def test_with_capital_letter_and_no_full_stop():
    result = check_sentence_grammer("Hello this is a nice day")
    assert result == False

#This tests empty string
def test_checking_empty_string():
    with pytest.raises(Exception) as e:
        check_sentence_grammer("")
    error_message = str(e.value)
    assert error_message == "No text to check."