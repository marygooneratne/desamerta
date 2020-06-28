import Transformation
import rule.transformation.transfer_util as tu


class High(Transformation):

    def __init__(self):
        super().__init__()

    def execute(self, date):
        return self.children[0].excute(date).highs[0]
