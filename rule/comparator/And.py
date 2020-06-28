import Comparator

class And(Comparator):
    def __init__(self):
        super().__init__()
    
    def execute(self, date=None):
        self.value = 1 if self.children[0].value == 1 and self.children[1].value == 1 else 0