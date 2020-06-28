import Transformation
import rule.transformation.transfer_util as tu


class ASI(Transformation):

    def __init__(self):
        super().__init__()

    def execute(self, date):
        return tu.accumulative_swing_index(self.children[0].excute(date))
