from abc import ABC, abstractmethod
from rule.Node import Node
NUM_CHILDREN = 1

class Base(Node):
    def __init__(self):
        super().__init__(num_children=NUM_CHILDREN)

    def execute(self, date=None):
        return self.children[0].execute()