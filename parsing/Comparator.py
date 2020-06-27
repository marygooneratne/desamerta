from abc import ABC, abstractmethod

class Comparator:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2
    
    @abstractmethod
    def is_true(self):
        pass