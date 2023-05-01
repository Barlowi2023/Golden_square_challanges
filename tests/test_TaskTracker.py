import pytest
from lib.TaskTracker import *

"""
Initially, there are no tasks
"""
def test_initially_has_no_tasks():
    tasktracker = TaskTracker()
    assert tasktracker.list_incomplete() == []
# => []

"""
When we add a task
It is reflected in the list of tasks
"""
def test_if_we_add_a_single_task():
    tasktracker = TaskTracker()
    tasktracker.add_todo("walk the dog")
    assert tasktracker.list_incomplete() == ["walk the dog"]
# => ["walk the dog"]

"""
When we add multiple tasks
They are all reflected in the list of tasks
"""
def test_if_we_add_multiple_tasks():
    tasktracker = TaskTracker()
    tasktracker.add_todo("walk the dog")
    tasktracker.add_todo("go shopping")
    tasktracker.add_todo("make the dinner")
    assert tasktracker.list_incomplete() == ["walk the dog", "go shopping", "make the dinner"]
# => ["walk the dog", "go shopping", "make the dinner"]

"""
When we add multiple tasks
And mark one as complete
It disappears from the list
"""
def test_if_we_mark_one_complete():
    tasktracker = TaskTracker()
    tasktracker.add_todo("walk the dog")
    tasktracker.add_todo("go shopping")
    tasktracker.add_todo("make the dinner")
    tasktracker.mark_complete(1)
    assert tasktracker.list_incomplete() == ["walk the dog", "make the dinner"]
# => ["walk the dog", "make the dinner"]

"""
If we try to mark a task as complete that does not exist (lower boundary)
It raises an error
"""
def test_lower_boundary_raises_exception_error():
    tasktracker = TaskTracker()
    tasktracker.add_todo("walk the dog")
    with pytest.raises(Exception) as e:
        tasktracker.mark_complete(-1)
    error_message = str(e.value)    
    assert error_message == "Error this value is lower than the boundary limit"
    # => Raises and error
    assert tasktracker.list_incomplete() == ["walk the dog"]
    # => check the original value is preserved ["walk the dog"]


"""
If we try to mark a task as complete that does not exist (upper boundary)
It raises an error
"""
def test_upper_boundary_raises_exception_error():
    tasktracker = TaskTracker()
    tasktracker.add_todo("walk the dog")
    with pytest.raises(Exception) as e:
        tasktracker.mark_complete(1)
    error_message = str(e.value)
    assert error_message == "Error this value is greater than the boundary limit"
    # => Raises and error
    assert tasktracker.list_incomplete() == ["walk the dog"] 
    # => check that the original value is preserved ["walk the dog"]