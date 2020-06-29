class Trades():
    def __init__(self, raw_json):
        self.asset = raw_json["asset"]
        self.action = raw_json["action"]
        self.quantity = raw_json["quantity"]
        self.history = []
    
    def execute(self, date):
        price = 0
        # price = Data.get(self.asset).get_price(date)
        self.history.append(
            {
                "date": date,
                "trades": [
                    {
                        "asset": self.asset,
                        "quantity": self.quantity,
                        "price": price,
                        "action": self.action
                    }
                ]
            }
        )
    
    def get_history(self):
        return self.history
