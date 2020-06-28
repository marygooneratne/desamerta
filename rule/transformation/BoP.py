import Transformation
import rule.transformation.transfer_util as tu


class BoP(Transformation):

    def __init__(self):
        super().__init__()

    def execute(self, date):
        return tu.balance_of_power(self.children[0].excute(date))[0]
