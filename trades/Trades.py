
class Trades():
    def __init__(self, raw_json):
        self.asset = raw_json["asset"]
        self.action = raw_json["action"]
        self.quantity = raw_json["quantity"]
        self.history = []
    
    def execute(self, date):
        ## My thought is, we could run through and make an array of these happening, then go back and do the finance stuff. It's confusing if you want to keep track of everything, price isnt enough, so lets do this first, then feed this into another method that calculates returns, etc.
        self.history.append(
            {
                "date": date,
                "trades": [
                    {
                        "asset": self.asset,
                        "quantity": self.quantity,
                        "action": self.action
                    }
                ]
            }
        )
    
    def get_history(self):
        return self.history
