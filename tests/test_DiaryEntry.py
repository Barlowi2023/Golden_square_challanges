import pytest
from lib.DiaryEntry import DiaryEntry

"""
given an empty title and contents
raises and error
"""
def test_errors_on_empty_title_and_contents():
    with pytest.raises(Exception) as e:
        DiaryEntry("","")
    assert str(e.value) == "Diary entries must have a title or contents"

"""
given a title and contents
#format - returns a formatted entry, like:
"My title: These are the contents"
"""
def test_format_with_title_and_contents():
    diaryentry = DiaryEntry("My Title", "Some contents")
    result = diaryentry.format()
    assert result == "My Title: Some contents"


"""
given a title and contents
#count_words - returns the number of words in the title and contents
"""
def test_counts_all_words_in_title_and_contents():
    diaryentry = DiaryEntry("My Title", "Some contents")
    result = diaryentry.count_words()
    assert result == 4

"""
given wpm of 2
and text with 2 words
#reading_time - returns 1 minute
"""
def test_reading_time_with_two_wpm_and_two_words():
    diaryentry = DiaryEntry("My Title", "one two")
    result = diaryentry.reading_time(2)
    assert result == 1

"""
given wpm of 2
and text with 3 words
#reading_time - returns 2 minute
"""
def test_reading_time_with_two_wpm_and_two_words():
    diaryentry = DiaryEntry("My Title", "one two three")
    result = diaryentry.reading_time(2)
    assert result == 2

    """
given wpm of 2
and text with 4 words
#reading_time - returns 2 minutes
"""
def test_reading_time_with_two_wpm_and_two_words():
    diaryentry = DiaryEntry("My Title", "one two three four")
    result = diaryentry.reading_time(2)
    assert result == 2

"""
Give a wpm  of 0
#reading_time Raises an error
"""
def test_reading_time_wmp_of_zero():
    diaryentry = DiaryEntry("My Title", "one two three")
    with pytest.raises(Exception) as e:
        diaryentry.reading_time(0)
    assert str(e.value) == "Cannot calculate a reading time with wpm of 0"


"""
Given a contents of 6 words
and a WPM of 2
and a minutes of 1
#reading_chunk returns the first two words
"""
def test_reading_chunk_with_two_wpm_and_two_minutes():
    diaryentry = DiaryEntry("My Title", "one two three four five six")
    assert diaryentry.reading_chunk(2, 1) == "one two"

    """
Given a contents of 6 words
and a WPM of 2
and a minutes of 1
#reading_chunk returns the first two words each time until the loop ends
"""
def test_reading_chunk_with_two_wpm_and_two_minutes():
    diaryentry = DiaryEntry("My Title", "one two three four five six")
    assert diaryentry.reading_chunk(2, 1) == "one two"
    assert diaryentry.reading_chunk(2, 1) == "three four"
    assert diaryentry.reading_chunk(2, 1) == "five six"
    assert diaryentry.reading_chunk(2, 1) == "one two"
