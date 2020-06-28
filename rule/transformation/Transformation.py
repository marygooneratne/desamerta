from abc import ABC, abstractmethod


class Transformation(Node):
    NUM_CHILDREN = 1

    def __init__(self):
        super().__init__(num_children=NUM_CHILDREN)

    @abstractmethod
    def execute(self):
        pass
