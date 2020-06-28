import Transformation
import rule.transformation.transfer_util as tu


class MACDIndicator(Transformation):

    def __init__(self):
        super().__init__()

    def execute(self, date):
        return tu.macd_indicator(self.children[0].excute(date).closes, self.params['slow_period'], self.params['fast_period'])[0]
