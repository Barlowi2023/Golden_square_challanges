# Parameters: one, a string
# Rules:
#   - It must be longer than 7 characters (8 is fine)
#   - It must contain at least one of the following special characters: `!`, `@`,
#     `$`, `%` or `&`
# Returns: a boolean (True if valid, False otherwise)
# Example:
#   Call:    is_valid("1234567")
#   Returns: False
#   Call:    is_valid("12345678")
#   Returns: False
#   Call:    is_valid("12345!78")
#   Returns: True

# == YOUR CODE ==


################
#Refactored code
################

def is_valid(password):
    #Define special characters
    sc = ["!", "@", "$", "%", "&"]
    #Validate the password length and check for any special characters
    if len(password) > 7 and any([x in password for x in sc]):
        print("Password is Valid!")
        return True
    else:
        print ("Password is invalid! Either the password length is too short or the password doesn't contain a special character")
        return False


######################
# Original Code Below
######################

# def is_valid(password):
    #validate the password length
    # password_length = len(password)
    # if password_length > 7:
    #     print("Password is a valid length")
    #     password_l_status = 1
    # else:
    #     print("Password is to short")
    #     password_l_status = 2

    #Validate whether the password contains a special character
    # if "!" in password or "@" in password or "$" in password or "%" in password or "&" in password:
    #     print("Password contains at least one special character")
    #     password_sc_status = 1
    # else:
    #     print("Password does not contain any special characters")
    #     password_sc_status = 2

    #Determin overall success
    # if password_l_status == 1 and password_sc_status == 1:
    #     print("password is valid")
    #     return True
    # elif password_l_status == 2 and password_sc_status == 2:
    #     print("both")
    #     return False
    # elif password_l_status == 2 :
    #     print("Password is not valid! Please increase the length to 8 charcters or more")
    #     return False
    # elif password_sc_status == 2:
    #     print("Password is not valid! Please include at least one special character")
    #     return False
    
    

test1 = is_valid("1234567")
print(test1)

test2 = is_valid("12345678")
print(test2)

test3 = is_valid("12345!78")
print(test3)