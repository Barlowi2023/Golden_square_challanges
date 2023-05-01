import pytest

from lib.PasswordChecker import *

#test if password is greater than 8
def test_if_greater_than_8():
    passwordchecker = PasswordChecker()

    result = passwordchecker.check("123456789")
    assert result == True

#test if password is too short and check the exception message is correct
def test_if_password_is_too_short():
    passwordchecker = PasswordChecker()
    with pytest.raises(Exception) as e:
        passwordchecker.check("1234567")
    error_message = str(e.value) 
    assert error_message == "Invalid password, must be 8+ characters."