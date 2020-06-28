import Transformation
import rule.transformation.transfer_util as tu


class Trix(Transformation):

    def __init__(self):
        super().__init__()

    def execute(self, date):
        return tu.trix(self.children[0].excute(date).closes)[0]
