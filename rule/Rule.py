import Comparator
import Computation
import Base
import Constant
# example_json = {
#   "transformation": "slope",
#   "transformaton": "MACD",
#   "asset": "AAPL"
#   "comparator": "greater than",
#   "constant": "0",
#   "comparator": "and",
#   "transformation": "MACD",
#   "asset": "AAPL",
#   "comparator": "equalto",
#   "transformation: "moving average"
#   "transformation: "MACD",
#   "asset": "AAPL"}

class Rule():
    def __init__(self, raw_json, date):
        self.raw_json = raw_json
        self.rule = Base()
    
    def build():
        cur = self.rule
        for key, value in raw_json:
            if not cur.populated():
                # new = class value of type key
                # cur.addchild(new)


        return


    def execute():
        return
