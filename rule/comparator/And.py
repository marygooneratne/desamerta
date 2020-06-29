from rule.comparator.Comparator import Comparator

class And(Comparator):
    def __init__(self):
        super().__init__()
    
    def execute(self, date=None):
        self.value = 1 if self.children[0].execute() == 1 and self.children[1].execute() == 1 else 0
        return self.value
    
    def add_child(self, child):
        if isinstance(child, Comparator):
            return super().add_child(child)
        else:
            return False