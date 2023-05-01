import math
class DiaryEntry():
    def __init__(self, title, contents):
        # Parameters:
        #   title: string
        #   contents: string
        if title == "" or contents == "":
            raise Exception("Diary entries must have a title or contents")
        self.title = title
        self.contents = contents
        self.words_read = 0

    def format(self):
        # Returns:
        #   A formatted diary entry, for example:
        #   "My Title: These are the contents"
        return f"{self.title}: {self.contents}"
    
    def count_words(self):
        #create a new variable called words containing the result of format() split into a string
        words = self.format().split()
        return len(words)
        # Returns:
        #   int: the number of words in the diary entry

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.
        if wpm == 0:
            raise Exception("Cannot calculate a reading time with wpm of 0")
        contents_word_count = len(self.contents.split())
        return math.ceil(contents_word_count / wpm)
        

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
        string_list = self.contents.split()

        """
        This is saying if the words read is greater than or equal to the length of our string
        list (so basically the words available) then bring the words ready back to zero.
        """
        if self.words_read >= len(string_list): 
            self.words_read = 0
        """
        This is where we start reading
        """
        start_chunk = self.words_read 
        """
        We end the chunk by adding the number of words to the amount read
        """
        end_chunk = self.words_read + no_of_words 
        """
        This counts from the start chunk to the end chunk.
        """
        reading_chunks = string_list[start_chunk:end_chunk] 
        print(f"Before it updates, words read is: {self.words_read}")
        """
        Now the words read is equal to the end chunk, so that when we go back to the beginning
        it will say words read is now increased. (We didn't need to do self.words_read += end_chunk)
        """
        self.words_read = end_chunk 
        print(f"After it updates, words read is: {self.words_read}")
        print(no_of_words)
        """
        Join the words so its not a list.
        """
        return " ".join(reading_chunks) 




