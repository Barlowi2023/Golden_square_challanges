
1. Describe the Problem
Put or write the user story here. Add any clarifying notes you might have.

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

2. Design the Function Signature
Include the name of the function, its parameters, return value, and side effects.

# EXAMPLE

def echeck_sentence_grammer(text):

    Parameters:
        text: a string containing words

    Returns: (state the return value and its type)
        boolean,  True if valid False otherwise

    Side effects:
        This function doesn't print anything or have any other side-effects


3. Create Examples as Tests
Make a list of examples of what the function will take and return.

# EXAMPLE

"""
Given a valid senetence with a capital letter and a full stop
It returns True
"""
check_sentence_grammer("Hello this is a nice day. ") => True

"""
Given a valid senetence with a capital letter and a question mark
It returns True
"""
check_sentence_grammer("Hello this is a nice day? ") => True

"""
Given an invalid sentence with a capital letter and no full stop
It returns False
"""
check_sentence_grammer("Hello this is a nice day") => False

"""
Given an invalid sentence with no capital letter and a full stop
It returns False
"""
check_sentence_grammer("hello this is a nice day.") => False


Encode each example as a test. You can add to the above list as you go.

4. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.

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
    assert result == True

"""
Given an invalid sentence with no capital letter and a full stop
It returns False
"""
def test_with_capital_letter_and_no_full_stop():
    result = check_sentence_grammer("Hello this is a nice day")
    assert result == True