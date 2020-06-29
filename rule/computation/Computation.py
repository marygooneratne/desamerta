from abc import ABC, abstractmethod
from rule.Node import Node

NUM_CHILDREN = 2

class Computation(Node):
    def __init__(self):
        super().__init__(num_children=NUM_CHILDREN)

    @abstractmethod
    def execute(self, date=None):
        pass