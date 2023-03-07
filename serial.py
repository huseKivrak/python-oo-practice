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
    def __init__(self, start):
        """ Creates instance of SerialGenerator from start, sets call status
         to False, stores start value for reset """
        self.start = start
        self.incr_num = start - 1


    def generate(self):
        """If hasn't been called, returns start value. Otherwise, returns
        sequential value """
        self.incr_num = self.incr_num + 1
        return self.incr_num

    def reset(self):
        """ Reassigns initial value and toggles call status """
        self.incr_num = self.start - 1
