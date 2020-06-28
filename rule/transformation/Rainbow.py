import Transformation
import rule.transformation.transfer_util as tu


class Rainbow(Transformation):

    def __init__(self):
        super().__init__()

    def execute(self, date):
        return [i[0] for i in tu.rainbow_ma(self.children[0].excute(date).closes, self.params['periods'])]
