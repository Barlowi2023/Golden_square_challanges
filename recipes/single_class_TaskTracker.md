Class Design Recipe

1. Describe the Problem
As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

2. Design the Class Interface
Include the initializer, public properties, and public methods with all parameters, return values, and side-effects.

# EXAMPLE

class TaskTracker:

    def __init__(self):
        self._task_list =[]    

    def Add_todo(self, todo):
        # Parameters:
        #  todo: string representing a task
        # Returns:
        #  Nothing
       
        #   If nothing is given raise an exception
        pass

    def list_incomplete(self):
        #Parameters: 
        # None
        #Returns:
        # A list of incomplete tasks
        pass

    def mark_complete(self, index):
        # Parameters:
        # Index: an integer representing the task to complete
        # Side effects:
        # Removes the task at index from the list of tasks
        pass
        
3. Create Examples as Tests
Make a list of examples of how the class will behave in different situations.

# EXAMPLES

"""
Initially, there are no tasks
"""
tasktracker = TaskTracker()
tracker.list_incomplete() 
# => []

"""
When we add a task
It is reflected in the list of tasks
"""
tasktracker = TaskTracker()
tasktracker.add_todo("walk the dog")
tasktracker.list_incomplete() 
# => ["walk the dog"]

"""
When we add multiple tasks
They are all reflected in the list of tasks
"""
tasktracker = TaskTracker()
tasktracker.add_todo("walk the dog")
tasktracker.add_todo("go shopping")
tasktracker.add_todo("make the dinner")
tasktracker.list_incomplete() 
# => ["walk the dog", "go shopping", "make the dinner"]

"""
When we add multiple tasks
And mark one as complete
It disappears from the list
"""
tasktracker = TaskTracker()
tasktracker.add_todo("walk the dog")
tasktracker.add_todo("go shopping")
tasktracker.add_todo("make the dinner")
tasktracker.mark_complete(1)
tasktracker.list_incomplete() 
# => ["walk the dog", "make the dinner"]

"""
If we try to mark a task as complete that does not exist (lower boundary)
It raises an error
"""
tasktracker = TaskTracker()
tasktracker.add_todo("walk the dog")
tasktracker.mark_complete(-1)
# => Raises and error
tasktracker.list_incomplete() 
# => check the original value is preserved ["walk the dog"]


"""
If we try to mark a task as complete that does not exist (upper boundary)
It raises an error
"""
tasktracker = TaskTracker()
tasktracker.add_todo("walk the dog")
tasktracker.mark_complete(1)
# => Raises and error
tasktracker.list_incomplete() 
# => check that the original value is preserved ["walk the dog"]




4. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.