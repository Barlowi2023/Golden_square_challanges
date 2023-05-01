import pytest
from lib.single_class_challenge_02_MusicTracker import *

"""
Initially, there are no music tracks
"""
def test_initially_has_no_music_tracks():
    musictracker = MusicTracker()
    assert musictracker.list_music() == []
# => []

"""
When we add a music task
It is reflected in the list of music tracks
"""
def test_when_we_add_a_single_track():
    musictracker = MusicTracker()
    musictracker.add_music("Let it be")
    assert musictracker.list_music() == ["Let it be"]
    # => ["Let it be"]

"""
When we add multiple music tracks
They are all reflected in the list of music tracks
"""
def test_when_we_add_multiple_tracks():
    musictracker = MusicTracker()
    musictracker.add_music("Let it be")
    musictracker.add_music("Twist and Shout")
    musictracker.add_music("Help!")
    musictracker.add_music("Here Comes the Sun")
    assert musictracker.list_music() == ["Let it be", "Twist and Shout", "Help!", "Here Comes the Sun"]
    # => ["Let it be", "Twist and Shout", "Help!', "Here Comes the Sun"]

"""
If we try to add a music track that already exists
It raises an error
"""
def test_raises_exception_error_if_task_already_exists():
    musictracker = MusicTracker()
    musictracker.add_music("Let it be")
    with pytest.raises(Exception) as e:
        musictracker.add_music("Let it be")
    error_message = str(e.value)
    assert error_message == "This track already exists!"
    # => check that the duplicate music track isn't added ["Let it be"]
    assert musictracker.list_music() == ["Let it be"]