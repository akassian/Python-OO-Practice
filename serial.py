"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=100):
        """
        Initialize, set start and
        accumulator variables
        """
        self.start = start
        self.accumulator = start

    def __repr__(self):
        """
        Describes instance and its start and current values
        """
        return f"<SerialGenerator start={self.start} next={self.accumulator}>"

    def generate(self):
        """
        Returns accumulator value and increments accumulator
        """
        self.accumulator += 1
        return self.accumulator - 1

    def reset(self):
        """
        Resets instance to its original start values
        """
        self.accumulator = self.start
