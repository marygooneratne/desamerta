from abc import ABC, abstractmethod

class Node:
    def __init__(self, value=None, children=None, num_children=0, params={}):
        self.children = [] if children is None else children
        self.value = value
        self.num_children = num_children
        self.params = params

    def add_child(self,obj):
        self.children.append(obj)
        return True

    def get_children(self):
        return self.children
    
    def executed(self):
        return self.value is not None

    def populated(self):
        return len(self.children) == self.num_children
    
    @abstractmethod
    def execute(self, date=None):
        pass
