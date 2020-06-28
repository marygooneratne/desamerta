import Transformation
import rule.transformation.transfer_util as tu


class SMA(Transformation):

    def __init__(self):
        super().__init__()

    def execute(self, date):
        return tu.sma(self.children[0].excute(date).closes, self.params['period'])[0]
