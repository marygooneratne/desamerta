import Constant

class Number(Constant):
    def __init__(self, value):
        super().__init__()
        self.value = value
    
    def execute(self, date=None):
        return