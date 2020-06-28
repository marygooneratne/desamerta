import Transformation
import rule.transformation.transfer_util as tu


class ROC(Transformation):

    def __init__(self):
        super().__init__()

    def execute(self, date):
        return tu.roc(self.children[0].excute(date).closes)[0]
