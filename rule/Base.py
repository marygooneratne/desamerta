from abc import ABC, abstractmethod

class Base(Node):
    NUM_CHILDREN = 1
    def __init__(self):
        super().__init__(num_children=NUM_CHILDREN)

    def execute(self):
        return self.children[0].value