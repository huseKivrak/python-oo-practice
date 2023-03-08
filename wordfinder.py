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
        """Opens file at path"""
        return open(f"{self.path}", "r")


    def words_read(self):
        """adds read lines to words"""
        return [word[:-1] for word in self.file]

    def len_of_words_read(self):
        """Returns length of word list"""
        return len(self.words)

    def random(self):
        """Returns random words from words"""
        return choice(self.words)


class SpecialWordFinder(WordFinder):
    """defines SpecialWordFinder instances, extends WordFinder"""

    def __init__(self, path):
        """constructs SpecialWordFinderInstances, adding real_words property"""
        super().__init__(path)
        self.real_words = self.get_words()


    def get_words(self):
        """Checks for and returns words that are not comments or blank lines"""
        reals = []
        for line in self.words:
            if not line.startswith('#') and line != "":
                reals.append(line)

        return reals