from Model import Model
import datetime as dt
from rule.Rule import Rule

rule_json1 = [
["constant", "3"],
["computation", "add"],
["constant", "27"],
["comparator", "greater than"],
["constant", "15"],
["comparator", "and"],
["constant", "100"],
["comparator", "less than"],
["constant", "13"],
["comparator", "or"],
["constant", "13"],
["comparator", "less than"],
[ "constant", "42"]]

rule_json2 = [
  ["constant", "2"],
  ["computation", "add"],
  ["parentheses", "left"],
  ["constant", "6"],
  ["computation", "divide"],
  ["constant", "2"],
  ["parentheses", "right"],
  ["comparator", "less than"],
  ["constant", "5"]
]

rule_json3 = [
  ["constant", "2"],
  ["computation", "add"],
  ["constant", "6"],
  ["computation", "divide"],
  ["constant", "2"],
  ["comparator", "less than"],
  ["constant", "5"]
]

trade_json = {
  "asset": "AAPL",
  "quantity": "30",
  "action": "buy"
}

example_json1 = {
    "rule": rule_json2,
    "trade": trade_json
}

example_json2 = {
    "rule": rule_json2,
    "trade": trade_json
}

rule1 = Rule(rule_json2)
rule2 = Rule(rule_json3)
rule1.print()
rule2.print()
print(rule1.execute())
print(rule2.execute())