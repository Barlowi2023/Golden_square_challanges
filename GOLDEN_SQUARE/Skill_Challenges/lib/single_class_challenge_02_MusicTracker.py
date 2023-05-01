class MusicTracker:

    def __init__(self):
        self._music_list =[]    

    def add_music(self, track):
        # Parameters:
        #  track: string representing a music track
        # Returns:
        #  Nothing
        # Action:
        #  If it is a new track then it is appended to the self._music_list
        #  If the track already exists in the self._music_list then it raises and exception
        if track in self._music_list:
            raise Exception("This track already exists!")
        else:
            self._music_list.append(track)
        print(f"The track: {track} has been added")

    def list_music(self):
        #Parameters: 
        # None
        #Returns:
        # A list of music tracks
        print(*self._music_list, sep = "\n")
        return self._music_list
