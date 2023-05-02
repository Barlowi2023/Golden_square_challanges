# == INSTRUCTIONS ==
#
# In these exercises you will define your own functions based on some
# requirements.
#
# The requirements will always start with the name of the function. Use this
# name exactly or the tests won't be able to find it.
#
# Then there will be a description of what the function should do.
# Note that some solutions will require more than one line of code.
#
# Here is an example of the rules:
#
# Method name: add_ten
# Purpose: adds ten to the given number
# Rules:
#   Takes one number as an arg
#   Adds ten and returns the new value
# Example:
#   Call:    add_ten(5)
#   Returns: 15

# And here is an example of a correct solution:

def add_ten(number):
    new_number = number + 10
    return new_number

# Let's get started.

# == EXERCISES ==

# Method name: say_hello
# Purpose: returns the string 'hello'
# Arguments: none
# Example:
#   Call:    say_hello()
#   Returns: "hello"
def say_hello():
    return "hello"

Test1 = say_hello()
print(Test1)


# Method name: say_goodbye
# Purpose: returns the string 'goodbye'
# Arguments: none
# Example:
#   Call:    say_goodbye()
#   Returns: "goodbye"
def say_goodbye():
    return "goodbye"

Test2 = say_goodbye()
print(Test2)


# Method name: say_hello_to
# Purpose: greets the given name
# Arguments: one string
# Example:
#   Call:    say_hello_to("Sam")
#   Returns: "Hello, Sam!"
def say_hello_to(name):
    return f"Hello, {name}!"

Test3 = say_hello_to("Sam")
print(Test3)

# Method name: say_goodbye_to
# Purpose: says goodbye to the given name
# Arguments: one string
# Example:
#   Call:    say_goodbye_to("Sam")
#   Returns: "Goodbye, Sam!"
def say_goodbye_to(name):
    return f"Goodbye, {name}!"

Test4 = say_goodbye_to("Sam")
print(Test4)


# Method name: square
# Purpose: multiplies the given number by itself
# Arguments: one number
# Example:
#   Call:    square(5)
#   Returns: 25
def square(number):
    return number*number

Test5 = square(5)
print(Test5)


# Method name: divisible_by_three
# Purpose: returns true if the given number is divisible by three
# Arguments: one number
# Example:
#   Call:    divisible_by_three(9)
#   Returns: True
#   Call:    divisible_by_three(10)
#   Returns: False
def divisible_by_three(number):
    if number % 3 == 0:
        return True
    else:
        return False
    
Test6 = divisible_by_three(9)
print(Test6)

Test7 = divisible_by_three(10)
print(Test7)


# Method name: add
# Purpose: adds two numbers together
# Arguments: two numbers
# Example:
#   Call:    add(5, 10)
#   Returns: 15
def add(num1, num2):
    return num1+num2

Test8 = add(5,10)
print(Test8)



# Method name: multiply
# Purpose: multiplies two numbers together
# Arguments: two numbers
# Example:
#   Call:    multiply(5, 10)
#   Returns: 50
def multiply(num1, num2):
    return num1*num2

Test9 = multiply(5,10)
print(Test9)


# Method name: add_number_strings
# Purpose: adds two numbers given as strings
# Arguments: two strings
# Example:
#   Call:    add_number_strings("5", "10")
#   Returns: 15
# Note: return value should be a number, not a string
def add_number_strings(string1, string2):
    string_num1 = int(string1)
    string_num2 = int(string2)
    return string_num1 + string_num2

Test10 = add_number_strings("5", "10")
print(Test10)



# Method name: multiply_number_strings
# Purpose: multiplies two numbers given as strings
# Arguments: two strings
# Example:
#   Call:    multiply_number_strings("5", "10")
#   Returns: 50
# Note: return value should be a number, not a string
def multiply_number_strings(string1, string2):
    string_num1 = int(string1)
    string_num2 = int(string2)
    return string_num1 * string_num2

Test11 = multiply_number_strings("5", "10")
print(Test11)


# Method name: both_odd
# Purpose: returns true if both numbers are odd
# Arguments: two numbers
# Example:
#   Call:    both_odd(5, 11)
#   Returns: True
#   Call:    both_odd(5, 10)
#   Returns: False
#   Call:    both_odd(6, 10)
#   Returns: False
def both_odd(num1, num2):
    if num1 %2 != 0 and num2 %2 != 0:
        return True
    else:
        return False
    
Test12 = both_odd(5,11)
print(Test12)

Test13 = both_odd(5,10)
print(Test13)

Test14 = both_odd(6,10)
print(Test14)


# Method name: both_even
# Purpose: returns true if both numbers are even
# Arguments: two numbers
# Example:
#   Call:    both_even(4, 10)
#   Returns: True
#   Call:    both_even(5, 10)
#   Returns: False
#   Call:    both_even(5, 11)
#   Returns: False
def both_even(num1, num2):
    if num1 %2 == 0 and num2 %2 == 0:
        return True
    else:
        return False
    
Test15 = both_even(4,10)
print(Test15)

Test16 = both_even(5,10)
print(Test16)

Test17 = both_even(5,11)
print(Test17)


# Method name: one_odd
# Purpose: returns true if at least one number is odd
# Arguments: two numbers
# Example:
#   Call:    one_odd(5, 10)
#   Returns: True
#   Call:    one_odd(4, 11)
#   Returns: True
#   Call:    one_odd(4, 8)
#   Returns: False
def one_odd(num1, num2):
    if num1 %2 != 0 or num2 %2 != 0:
        return True
    else:
        return False
    
Test18 = one_odd(5,10)
print(Test18)

Test19 = one_odd(4,11)
print(Test19)

Test20 = one_odd(4,8)
print(Test20)    


# Method name: one_even
# Purpose: returns true if at least one number is even
# Arguments: two numbers
# Example:
#   Call:    one_even(5, 10)
#   Returns: True
#   Call:    one_even(4, 11)
#   Returns: True
#   Call:    one_even(5, 9)
#   Returns: False
def one_even(num1, num2):
    if num1 %2 == 0 or num2 %2 == 0:
        return True
    else:
        return False
    
Test21 = one_even(5, 10)
print(Test21)

Test22 = one_even(4, 11)
print(Test22)

Test23 = one_even(5, 9)
print(Test23) 



# Method name: truncate_string
# Purpose: truncates (shortens) a string to 10 characters
# Arguments: one string
# Rules:
#   If the string is longer than 10 characters
#   return the first 10 characters followed by '...'
#   If the string is 10 characters or less
#   return the whole string
# Example:
#   Call:    truncate_string("This is a long string")
#   Returns: "This is a ..."
#   Call:    truncate_string("Short")
#   Returns: "Short"

def truncate_string(string):
    #find the length of the string
    str_len = len(string)
    if str_len > 10:
        #slice to retrieve the first 10 characters
        return string[0:10] + "..."
    else:
        return string
    
Test24 = truncate_string("This is a long string")
print(Test24)

# Congrats, you're done with this file, go back to the Challenges README.
