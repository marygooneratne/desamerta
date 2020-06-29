from Model import Model
import datetime as dt
rule_json = [
{"constant": "3"},
{"computation": "add"},
{"constant": "27"},
{"comparator": "greater than"},
{"constant": "15"},
{"comparator": "and"},
{"constant": "100"},
{"comparator": "less than"},
{"constant": "13"},
{"comparator": "or"},
{"constant": "13"},
{"comparator": "less than"},
{ "constant": "42"}]

trade_json = {
  "asset": "AAPL",
  "quantity": "30",
  "action": "buy"
}

example_json = {
    "rule": rule_json,
    "trade": trade_json
}

model = Model(example_json)
print(model.execute(dt.datetime(2020,1,1), dt.datetime(2020,1,15)))