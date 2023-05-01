class DiaryEntry():
    def __init__(self, title, contents):
        # Parameters:
        #   title: string
        #   contents: string
       
        self.title = title
        self.contents = contents


    def format(self):
        # Returns:
        #   A formatted diary entry, for example:
        #   "My Title: These are the contents"
        formatted = f"{self.title}: {self.contents}"
        return formatted

    def count_words(self):
        return len(self.title.split()) + len(self.contents.split())
        # Returns:
        #   int: the number of words in the diary entry


    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.
        if self.count_words() == 2:
            return  1
        else:
            return int(self.count_words() / wpm)

    def reading_chunk(self, wpm, minutes):
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        no_of_words = wpm * minutes
        string_list = self.format().split()
        words_read = 0
        words_available = self.count_words()

        if words_read == 0:
            reading_chunk = string_list[0:no_of_words]
            words_read += no_of_words
            words_available -= words_read

            return reading_chunk
        
        


diaryentry = DiaryEntry(" ".join(["title" for i in range(0, 100)]), " ".join(["contents" for i in range(0, 100)]) )
print(diaryentry.format())
print(diaryentry.count_words())
print(diaryentry.reading_time(2))
print(diaryentry.reading_chunk(10, 2))