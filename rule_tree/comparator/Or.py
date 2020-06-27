import Comparator

class Or(Comparator):
    def __init__(self):
        super().__init__()
    
    def execute(self):
        self.value = 1 if self.children[0].value == 1 or self.children[1].value == 1 else 0