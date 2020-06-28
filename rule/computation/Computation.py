from abc import ABC, abstractmethod

class Computation(Node):
    NUM_CHILDREN = 2
    def __init__(self):
        super().__init__(num_children=NUM_CHILDREN)

    @abstractmethod
    def execute(self):
        pass