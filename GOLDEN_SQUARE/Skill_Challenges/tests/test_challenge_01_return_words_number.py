from lib.challenge_01_return_words_number import *

# Test function returns 0 if no string
def test_empty_string_returns_zero():
    counter = count_words('')
    assert counter == 0

# Test function function returns number of words in a string given

def test_return_number_words_in_string():
    counter = count_words('hello world')
    assert counter == 2

# # Test if empty string added to raise error
# def test_empty_string_added():
#     with pytest.raises(Exception) as e:
#         count_words('')
#     error_message = str(e.value)
#     assert error_message == "No string added"