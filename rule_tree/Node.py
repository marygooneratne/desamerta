from abc import ABC, abstractmethod

class Node():
    def __init__(self, value=None, children=[], num_params=0):
        self.children = children
        self.value = value
        self.num_params = num_params

    def add_child(self,obj):
        self.children.append(obj)

    def get_children(self):
        return self.children
    
    def executed(self):
        return self.value is not None

    def populated(self):
        return len(children) == num_params
    
    @abstractmethod
    def execute(self):
        pass
