import Comparator

class Add(Computation):
    def __init__(self):
        super().__init__()
    
    def execute(self):
        self.value = self.children[0].value + self.children[1].value