import Computation

class Add(Computation):
    def __init__(self):
        super().__init__()
    
    def execute(self, date=None):
        self.value = self.children[0].value + self.children[1].value