from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    def __init__(self, path):
        self.path = path
        self.file = self.open_file()
        self.words = self.words_read()
        self.words_length = self.len_of_words_read()
        print( f"{self.words_length} words read")

    def open_file(self):
        return open(f"{self.path}", "r")


    def words_read(self):
        return [word for word in self.file]

    def len_of_words_read(self):
        return len(self.words)

    def random(self):
        return choice(self.words)[2:-1]