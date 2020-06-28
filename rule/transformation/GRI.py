import Transformation
import rule.transformation.transfer_util as tu


class GRI(Transformation):

    def __init__(self):
        super().__init__()

    def execute(self, date):
        return tu.gop_range_index(self.children[0].excute(date), self.params['period'])[0]
