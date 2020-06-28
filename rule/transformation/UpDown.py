import Transformation
import rule.transformation.transfer_util as tu


class UpDown(Transformation):

    def __init__(self):
        super().__init__()

    def execute(self, date):
        return tu.calc_up_down(self.children[0].excute(date).closes, self.params['period'])[0]
