import Transformation
import rule.transformation.transfer_util as tu


class RSI(Transformation):

    def __init__(self):
        super().__init__()

    def execute(self, date):
        return tu.rsi(self.children[0].excute(date).closes, self.params['period'], self.params['type'])[0]
