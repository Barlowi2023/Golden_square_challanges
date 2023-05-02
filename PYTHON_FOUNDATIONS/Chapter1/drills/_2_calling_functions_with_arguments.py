# == INSTRUCTIONS ==
#
# These challenges are a bit trickier and, in some cases, will required a few
# lines of code. If you start to get a little stuck, take a step back and make
# a plan by breaking the overall task down into small steps.

# == EXERCISES ==

# Purpose: checks if a string starts with the letter a
# Example:
#   Call:    starts_with_the_letter_a("apple")
#   Returns: True
#   Call:    starts_with_the_letter_a("Apple")
#   Returns: True
#   Call:    starts_with_the_letter_a("Rock")
#   Returns: False
def starts_with_the_letter_a(string):
    if string.upper().startswith("A"):
        return True
    else:
        return False

Test1 = starts_with_the_letter_a("apple")
print(Test1) 

Test2 = starts_with_the_letter_a("Apple")
print(Test2)

Test3 = starts_with_the_letter_a("Rock")
print(Test3)


# Purpose: checks if a string ends with the letter a
# Example:
#   Call:    ends_with_the_letter_a("Java")
#   Returns: True
#   Call:    ends_with_the_letter_a("JAVA")
#   Returns: True
#   Call:    ends_with_the_letter_a("Python")
#   Returns: False
def ends_with_the_letter_a(string):
    if string.upper().endswith("A"):
        return True
    else:
        return False
    
Test4 = ends_with_the_letter_a("Java")
print(Test4)

Test5 = ends_with_the_letter_a("JAVA")
print(Test5)

Test6 = ends_with_the_letter_a("Python")
print(Test6)


# Purpose: checks if a string contains the word hello
# Example:
#   Call:    contains_hello("hello world")
#   Returns: True
#   Call:    contains_hello("HELLO WORLD")
#   Returns: True
#   Call:    contains_hello("world")
#   Returns: False
def contains_hello(string):
    if "hello" in string.lower():
        return True
    else:
        return False
    
Test7 = contains_hello("hello world")
print(Test7)

Test8 = contains_hello("HELLO WORLD")
print(Test8)

Test9 = contains_hello("world")
print(Test9)


# Purpose: replaces the word hello with the word goodbye
# Note: you don't need to worry about matching 'Hello' or 'HELLO' here
#       lowercase only is fine.
# Example:
#   Call:    substitute_hello_with_goodbye("hello folks")
#   Returns: "goodbye folks"
#   Call:    substitute_hello_with_goodbye("Hello folks")
#   Returns: "Hello folks"
def substitute_hello_with_goodbye(string):
    if "hello" in string:
        return string.replace("hello", "goodbye")
    else:
        return string
    
Test10 = substitute_hello_with_goodbye("hello folks")
print(Test10)

Test11 = substitute_hello_with_goodbye("Hello folks")
print(Test11)


# Purpose: removes the letter x from a string
# Example:
#   Call:    remove_x("xoxo")
#   Returns: "oo"
#   Call:    remove_x("OXO")
#   Returns: "OO"
def remove_x(string):
    if "x" in string:
        new_string = string.replace("x", "")
        return new_string
    if "X" in string:
        new_string = string.replace("X", "")
        return new_string
    else:
        print("No X's to remove")
        return string
    
Test12 = remove_x("xoxo")
print(Test12)

Test13 = remove_x("OXO")
print(Test13)

Test14 = remove_x("Ian")
print(Test14)


# Purpose: returns the first half of a string
# Example:
#   Call:    first_half("coding")
#   Returns: "cod"
# Note: you can assume the string will always have an even number of characters
def first_half(string):
    half_string_length = len(string)/2
    stop_point = int(half_string_length)
    return string[0:stop_point]

Test15 = first_half("coding")
print(Test15)


# Purpose: returns the second half of a string
# Example:
#   Call:    second_half("coding")
#   Returns: "ing"
# Note: you can assume the string will always have an even number of characters
def second_half(string):
    string_length = len(string)
    half_string_length = len(string)/2
    start_point = int(half_string_length)
    stop_point = string_length + 1
    return string[start_point:stop_point]

Test16 = second_half("coding")
print(Test16)


# Congrats, you're done with this file. Move on to the next one.
