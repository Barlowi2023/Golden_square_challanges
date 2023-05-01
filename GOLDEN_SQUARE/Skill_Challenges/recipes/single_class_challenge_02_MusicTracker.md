Class Design Recipe

1. Describe the Problem
As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

2. Design the Class Interface
Include the initializer, public properties, and public methods with all parameters, return values, and side-effects.

# EXAMPLE

class MusicTracker:

    def __init__(self):
        self._music_list =[]    

    def add_music(self, track):
        # Parameters:
        #  track: string representing a music track
        # Returns:
        #  Nothing
        pass

    def list_music(self):
        #Parameters: 
        # None
        #Returns:
        # A list of music tracks
        pass

        
3. Create Examples as Tests
Make a list of examples of how the class will behave in different situations.

# EXAMPLES

"""
Initially, there are no music tracks
"""
musictracker = MusicTracker()
musictracker.list_music() 
# => []

"""
When we add a music task
It is reflected in the list of music tracks
"""
musictracker = MusicTracker()
musictracker.add_music("Let it be")
musictracker.list_music() 
# => ["Let it be"]

"""
When we add multiple music tracks
They are all reflected in the list of music tracks
"""
musictracker = MusicTracker()
musictracker.add_music("Let it be")
musictracker.add_music("Twist and Shout")
musictracker.add_music("Help!")
musictracker.add_music("Here Comes the Sun")
musictracker.list_music()
# => ["Let it be", "Twist and Shout", "Help!', "Here Comes the Sun"]

"""
If we try to add a music task that already exists
It raises an error
"""
musictracker = MusicTracker()
musictracker.add_music("Let it be")
musictracker.add_music("Let it be")
# => Raises and error
musictracker.list_music() 
# => check that the duplicate music track isn't added ["Let it be"]



4. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.