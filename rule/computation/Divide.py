from rule.computation.Computation import Computation

class Divide(Computation):
    def __init__(self):
        super().__init__()
    
    def execute(self, date=None):
        self.value = self.children[0].execute() / self.children[1].execute()
        return self.value