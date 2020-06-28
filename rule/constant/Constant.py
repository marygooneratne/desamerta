from abc import ABC, abstractmethod

class Constant(Node):
    NUM_CHILDREN = 0
    def __init__(self):
        super().__init__(num_children=NUM_CHILDREN)
    
    @abstractmethod
    def execute(self, date=None):
        pass