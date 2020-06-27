from abc import ABC, abstractmethod

class Comparator(Node):
    NUM_CHILDREN = 2
    def __init__(self):
        super().__init__(num_children=NUM_CHILDREN)
    
    @abstractmethod
    def is_true(self):
        pass

    @abstractmethod
    def execute(self):
        pass