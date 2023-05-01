from lib.gratitudes import *

# Check for empty list
def test_1_empty_list():
    gratitudes = Gratitudes()
    assert gratitudes.format() == "Be grateful for: "

# Test for multiple strings input
def test_2_multiple_strings_input():
    gratitudes = Gratitudes()
    gratitudes.add('gratitude')
    gratitudes.add('johny')
    gratitudes.add('ben')
    assert gratitudes.format() == 'Be grateful for: gratitude, johny, ben'

# Test for longer string input
def test_3_multiple_strings_input():
    gratitudes = Gratitudes()
    gratitudes.add('sun and nature')
    assert gratitudes.format() == 'Be grateful for: sun and nature'






