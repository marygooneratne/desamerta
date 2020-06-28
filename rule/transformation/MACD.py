import Transformation
import rule.transformation.transfer_util as tu


class MACD(Transformation):

    def __init__(self):
        super().__init__()

    def execute(self, date):
        return tu.macd(self.children[0].excute(date).closes, self.params['slow_period'], self.params['fast_period'])[0]
