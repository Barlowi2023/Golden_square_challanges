import pytest
from lib.present import *

#test when we wrap an item we get it back when unwrapping
def test_wrap_and_unwrap():
    present = Present()
    present.wrap(33)
    assert present.unwrap() == 33

#test unwrap without wrapping
def test_unwrap_without_wrapping():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()

    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."

#Test if we try to wrap an alreaty wrapped present
def test_wrapping_already_wrapped():
    present = Present()
    present.wrap(44)
    with pytest.raises(Exception) as e:
        present.wrap(66)
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."

#test if the first wrapped value is unchanged

def test_first_wrapped_value_is_unchanged():
    present = Present()
    present.wrap(44)
    with pytest.raises(Exception) as e:
        present.wrap(66)
    
    assert present.unwrap() == 44