from rule.comparator.Comparator import Comparator

class GreaterThan(Comparator):
    def __init__(self):
        super().__init__()
    
    def execute(self, date=None):
        self.value = 1 if self.children[0].execute() > self.children[1].execute() else 0
        return self.value