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
        self.start = start
        self.ser_num = start
        self.has_been_called = False

    def generate(self):
        if self.has_been_called:
            self.ser_num + 1
            return self.ser_num
        else:
            self.has_been_called = True
            return self.start


    def reset(self):
        self.ser_num = self.start