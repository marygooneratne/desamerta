import Comparator

class Equals(Comparator):
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2
    
    def is_true(self):
        return self.value1 == self.value2