import Transformation
import rule.transformation.transfer_util as tu


class KST(Transformation):

    def __init__(self):
        super().__init__()

    def execute(self, date):
        return tu.kst(self.children[0].excute(date).closes)[0]
