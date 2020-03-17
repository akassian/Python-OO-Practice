"""Word Finder: finds random words from a dictionary."""
from random import choice


class WordFinder:
    """
    >>> wf = WordFinder("/usr/share/dict/words")
    235886 words read
    """

    def __init__(self, filepath):
        """
        Uses filepath to load words from file into self.words
        """
        self.filepath = filepath
        self.words = []
        self._load_data_()
        print(len(self.words), "words read")

    def __repr__(self):
        """
        Describes instance and its filepath and number of words
        """
        return f"<WordFinder filepath={self.filepath} \
            contains {len(self.words)} words>"

    def _load_data_(self):
        """
        Assums 1 word per line, reads file line by line
        """
        file = open(self.filepath)
        for line in file:
            self.words.append(line.strip())
        file.close()

    def random(self):
        """
        Returns a random word from self.words
        """
        return choice(self.words)


class RandomWordFinder(WordFinder):
    """
    >>> wf = RandomWordFinder("words.txt")
    4 words read
    >>> wf.random() in ["apple", "mango", "kale", "parsnips"]
    True
    >>> wf.random() in ["apple", "mango", "kale", "parsnips"]
    True
    >>> wf.random() in ["apple", "mango", "kale", "parsnips"]
    True
    >>> wf.random() in ["apple", "mango", "kale", "parsnips"]
    True

    """

    def __init__(self, filepath):
        """
        Call's parent constructor,
        uses filepathto load words
        from file into self.words
        """
        super().__init__(filepath)

    def _load_data_(self):
        """
        Called by __init__
        Overwrites parent's _load_data_
        to ignore comments and blank lines
        """
        file = open(self.filepath)
        for line in file:
            stripped = line.strip()
            if not (stripped.startswith("#") or len(stripped) == 0):
                self.words.append(stripped)
        file.close()
