import Transformation
import rule.transformation.transfer_util as tu


class Open(Transformation):

    def __init__(self):
        super().__init__()

    def execute(self, date):
        return self.children[0].excute(date).opens[0]
