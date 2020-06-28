import Transformation
import rule.transformation.transfer_util as tu


class ATR(Transformation):

    def __init__(self):
        super().__init__()

    def execute(self, date):
        return tu.average_true_range(self.children[0].excute(date))[0]
