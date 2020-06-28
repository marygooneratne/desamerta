import Transformation
import rule.transformation.transfer_util as tu


class PivotIndicator(Transformation):

    def __init__(self):
        super().__init__()

    def execute(self, date):
        return tu.prings_know_sure_thing(self.children[0].excute(date).closes)[0]
