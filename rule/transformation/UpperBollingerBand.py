import Transformation
import rule.transformation.transfer_util as tu


class LowerBollingerBand(Transformation):

    def __init__(self):
        super().__init__()

    def execute(self, date):
        return tu.bollinger_bands(self.children[0].excute(date), self.params['period'], self.params['stds'])[0][0]
