import Transformation
import rule.transformation.transfer_util as tu


class PivotPoint(Transformation):

    def __init__(self):
        super().__init__()

    def execute(self, date):
        return tu.pivot_points(self.children[0].excute(date))[0]
