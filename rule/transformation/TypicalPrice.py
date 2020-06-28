import Transformation
import rule.transformation.transfer_util as tu


class TypicalPrices(Transformation):

    def __init__(self):
        super().__init__()

    def execute(self, date):
        return tu.typical_prices(self.children[0].excute(date))[0]
