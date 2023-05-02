# == INSTRUCTIONS ==
#
# In these exercises you will define your own functions.
#
# Most functions will take a list or a dictionary as an argument, but some will
# take other arguments and some won't take any.
#
# The requirements will always start with the name of the function. Use this
# name exactly or the tests won't be able to find it.
#
# Then there will be a description of what the function should do. Note that
# some solutions will require more than one line of code.
#
# You won't find everything that you need in our materials. Use the Python Docs
# and Google liberally if you get stuck.

# == LIST EXERCISES ==

# Method name: first_element
# Purpose: returns the first element of the given list
# Arguments: one list
# Example:
#   Call:    first_element([1, 2, 3])
#   Returns: 1
def first_element(list):
    return list[0]

first_element([1, 2, 3])

# Method name: second_element
# Purpose: returns the second element of the given list
# Arguments: one list
# Example:
#   Call:    second_element([1, 2, 3])
#   Returns: 2
def second_element(list):
    return list[1]

second_element([1, 2, 3])


# Method name: last_element
# Purpose: returns the last element of the given list
# Arguments: one list
# Example:
#   Call:    last_element([1, 2, 3])
#   Returns: 3
def last_element(list):
    return list[-1]

last_element([1, 2, 3])


# Method name: first_two_elements
# Purpose: returns the first two elements of the given list
# Arguments: one list
# Example:
#   Call:    first_two_elements([1, 2, 3])
#   Returns: [1, 2]
def first_two_elements(list):
    new_list = list[:2]
    return new_list

first_two_elements([1, 2, 3])


# Method name: first_three_elements
# Purpose: returns the first three elements of the given list
# Arguments: one list
# Example:
#   Call:    first_three_elements([1, 2, 3, 4])
#   Returns: [1, 2, 3]
def first_three_elements(list):
    new_list = list[:3]
    return new_list

first_three_elements([1, 2, 3, 4])


# Method name: total
# Purpose: returns the sum of all the elements in the given list
# Arguments: one list
# Example:
#   Call:    total([1, 2, 3])
#   Returns: 6
def total(list):
    return sum(list)

total([1, 2, 3])


# Method name: lowest_number
# Purpose: returns the lowest number in the given list
# Arguments: one list
# Example:
#   Call:    lowest_number([4, 2, 6])
#   Returns: 2
def lowest_number(list):
    #sort the list
    list.sort()
    return list[0]

lowest_number([4, 2, 6])


# Method name: highest_number
# Purpose: returns the highest number in the given list
# Arguments: one list
# Example:
#   Call:    highest_number([4, 6, 2])
#   Returns: 6
def highest_number(list):
    #sort the list
    list.sort()
    return list[-1]

highest_number([4, 6, 2])


# Method name: the_beatles
# Purpose: returns the list ['john', 'paul', 'george', 'ringo']
# Arguments: none
# Example:
#   Call:    the_beatles()
#   Returns: ['john', 'paul', 'george', 'ringo']
def the_beatles():
    list = ['john', 'paul', 'george', 'ringo']
    return list

the_beatles()



# Method name: i_joined_the_beatles
# Purpose: adds the given name to the list ['john', 'paul', 'george', 'ringo']
# Arguments: one string
# Example:
#   Call:    i_joined_the_beatles('yoko')
#   Returns: ['john', 'paul', 'george', 'ringo', 'yoko']
def i_joined_the_beatles(new_string):
    list = ['john', 'paul', 'george', 'ringo']
    list.append(new_string)
    return list

i_joined_the_beatles('yoko')


# Method name: we_joined_the_beatles
# Purpose: adds the given names to the list ['john', 'paul', 'george', 'ringo']
# Arguments: one list
# Example:
#   Call:    we_joined_the_beatles(['yoko', 'stuart'])
#   Returns: ['john', 'paul', 'george', 'ringo', 'yoko', 'stuart']
def we_joined_the_beatles(new_list):
    list = ['john', 'paul', 'george', 'ringo']
    combined_list = list + new_list
    return combined_list

we_joined_the_beatles(['yoko', 'stuart'])

# Method name: remove_nones_from_list
# Purpose: removes all the None values from the given list
# Arguments: one list
# Example:
#   Call:    remove_nones_from_list([1, None, 2, None, 3])
#   Returns: [1, 2, 3]
def remove_nones_from_list(list):
    new_list = [i for i in list if i != None]
    return new_list

remove_nones_from_list([1, None, 2, None, 3])



# Method name: double_list
# Purpose: returns a list with all the elements of the given list repeated twice
# Arguments: one list
# Example:
#   Call:    double_list([1, 2, 3])
#   Returns: [1, 2, 3, 1, 2, 3]
def double_list(list):
    new_list = list + list
    return new_list

double_list([1, 2, 3])


# Method name: unique_elements
# Purpose: returns a list with all the unique elements of the given list
# Arguments: one list
# Example:
#   Call:    unique_elements([1, 2, 1, 3, 2, 3])
#   Returns: [1, 2, 3]
def unique_elements(list):
    new_list = []
    for i in list:
        if i not in new_list:
            new_list.append(i)
    return new_list

unique_elements([1, 2, 1, 3, 2, 3])


# Method name: add_to_list
# Purpose: adds the given element to the given list
# Arguments: one list and one element
# Example:
#   Call:    add_to_list(["a", "b", "c"], "d")
#   Returns: ["a", "b", "c", "d"]
def add_to_list(list, ele):
    list.append(ele)
    return list

add_to_list(["a", "b", "c"], "d")


# == DICTIONARY EXERCISES ==

# Method name: new_band_member
# Purpose: merges a given dictionary into an existing dictionary
# Arguments: one dictionary
# Note: {"vocalist": "miss piggy", "lead_guitar": "scooter"}
# Example:
#   Call:    new_band_member({"bass": "flea"})
#   Returns: {"vocalist": "miss piggy", "lead_guitar": "scooter", "bass": "flea"}
def new_band_member(new_member):
    band = {"vocalist": "miss piggy", "lead_guitar": "scooter"}
    band.update((new_member))
    return band

new_band_member({"bass": "flea"})

# Method name: all_values
# Purpose: returns a list of all the values in the given dictionary
# Arguments: one dictionary
# Example:
#   Call:    all_values({"a": 1, "b": 2, "c": 3})
#   Returns: [1, 2, 3]
def all_values(dict):
    return dict.values()

all_values({"a": 1, "b": 2, "c": 3})



# Method name: all_keys
# Purpose: returns a list of all the keys in the given dictionary
# Arguments: one dictionary
# Example:
#   Call:    all_keys({"a": 1, "b": 2, "c": 3})
#   Returns: ["a", "b", "c"]
def all_keys(dict):
    return dict.keys()


all_keys({"a": 1, "b": 2, "c": 3})


# Method name: remove_nones_from_dictionary
# Purpose: removes all pairs from a given dictionary where the value is None
# Arguments: one dictionary
# Example:
#   Call:    remove_nones_from_dictionary({"a": 1, "b": None, "c": 3})
#   Returns: {"a": 1, "c": 3}

def remove_nones_from_dictionary(dict):
    #Use dict comprehension to create a new dictionary excluding the nones
    new_dict = {k:v for k, v in dict.items() if v}
    return new_dict
    print(new_dict)
    #loop over dict to find all None values and delete the key value pairs from dict 
    # for key,value in dict.items():
    #     if value == None:
    #         del dict[key]
    # return dict

remove_nones_from_dictionary({"a": 1, "b": None, "c": 3})



# Method name: touch_in
# Purpose: creates a dictionary from a given tube station and time
# Arguments: two strings, one for the tube station and one for the time
# Example:
#   Call:    touch_in('Aldgate East', '2022/01/30 17:12')
#   Returns: {'entrypoint': 'Aldgate East', 'time': '2022/01/30 17:12'}
def touch_in(string1, string2):
    tube_station = {}
    tube_station["entrypoint"] = string1
    tube_station["time"] = string2
    return tube_station

touch_in('Aldgate East', '2022/01/30 17:12')