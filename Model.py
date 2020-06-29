from rule.Rule import Rule
from trades.Trades import Trades
# Trades object handles execution of single rule, holds price paid, total, etc



# trade_json = {
#   "asset": "AAPL",
#   "quantity": "30",
#   "action": "buy"
# }
# response_json = [{
#   "date": "12-01-2002",
#   "trades": [
#       {
#           "asset": "AAPL",
#           "quantity": "30",
#           "price": "300.42",
#           "action": "buy"]
#       }
#   ]
# },
# {
#   "date": "12-07-2002",
#   "trades": [
#       {
#           "asset": "AAPL",
#           "quantity": "30",
#           "price": "290.14",
#           "action": "buy"]
#       }
#   ]
# }
# ]

class Model():
    def __init__(self, raw_json):
        self.trade_json = raw_json["trade"]
        self.rule_json = raw_json["rule"]
        self.rule = Rule(raw_json["rule"])
        self.trades = Trades(raw_json["trade"])
    
    def execute(self, dates):
        for day in dates:
            if self.rule.execute(day) == 1:
                self.trades.execute(day)
        return self.trades.get_history()
    
    def get_total_trades(self):
        total = 0
        for day in self.trades.get_history():
            trades = day["trades"]
            for trade in trades:
                total += float(trade["quantity"])
    

    

