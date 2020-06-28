import Comparator

class Equals(Comparator):
    def __init__(self):
        super().__init__()
    
    def execute(self, date=None):
        self.value = 1 if self.children[0].value == self.children[1].value else 0