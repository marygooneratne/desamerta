from abc import ABC, abstractmethod

class Comparator(Node):
    NUM_PARAMS = 2
    def __init__(self):
        super().__init__(num_params=NUM_PARAMS)
    
    @abstractmethod
    def is_true(self):
        pass

    @abstractmethod
    def execute(self):
        pass