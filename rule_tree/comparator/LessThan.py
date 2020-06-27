import Comparator

class LessThan(Comparator):
    def __init__(self):
        super().__init__()
    
    def execute(self):
        self.value = 1 if self.children[0].value < self.children[1].value else 0