import Transformation
import rule.transformation.transfer_util as tu


class Move(Transformation):

    def __init__(self):
        super().__init__()

    def execute(self, date):
        return tu.ohlc(self.children[0].excute(date))[0]
