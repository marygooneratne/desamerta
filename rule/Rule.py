import importlib

from rule.comparator.Comparator import Comparator
from rule.computation.Computation import Computation
from rule.Base import Base
from rule.constant.Constant import Constant
from rule.constant.Number import Number
from rule.computation.Add import Add
from rule.comparator.And import And
from rule.comparator.Equals import Equals
from rule.comparator.GreaterThan import GreaterThan
from rule.comparator.LessThan import LessThan
from rule.comparator.Or import Or

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
NODE_TYPES = {
    "greaterthan": GreaterThan,
    "lessthan": LessThan,
    "and": And,
    "equalto": Equals,
    "number": Number,
    "add": Add,
    "or": Or
}
class Rule():
    def __init__(self, raw_json, dates=[]):
        self.raw_json = raw_json
        self.base_rule = Base()
        self.build()
    
    def build(self):
        leaf_stack = []
        parent_stack = []
        print(len(self.raw_json))
        for dictionary in self.raw_json:
            print('-----------------------------------------------------------------------------------')
            key = [entry for entry in dictionary][0]
            value = dictionary[key]
            print(key, value)

            if key == "constant":
                node = NodeFactory.create_node("number", value=float(value))
            else:
                node = NodeFactory.create_node(value)
            
            print("Created node with type ", type(node), ", value: ", node.value, ", children: ", node.children)

            if(self.is_leaf(node)):
                leaf_stack.append(node)
            else:
                parent_stack.append(node)

            print("PRE-REARRANGEMENT")
            print("leaf_stack: ", leaf_stack)
            print("parent_stack: ", parent_stack)
            unadded_leaves = []
            while len(leaf_stack) > 0 and len(parent_stack) > 0:
                parent = parent_stack.pop()
                leaf = leaf_stack.pop()
                if not parent.add_child(leaf):
                    print('appending')
                    unadded_leaves.append(leaf)
                if(self.is_leaf(parent)):
                    leaf_stack.append(parent)
                else:
                    parent_stack.append(parent)
                print("POST-REARRANGEMENT")
                print("leaf_stack: ", leaf_stack)
                print("parent_stack: ", parent_stack)
            leaf_stack = leaf_stack + unadded_leaves
        self.base_rule.add_child(leaf_stack.pop())
    
    def print_rule(self, node, level=0):
        ret = "\t"*level+(str(type(node)))+"\n"
        for child in node.children:
            ret += self.print_rule(child, level=level+1)
        return ret
    
    def print(self):
        print(self.print_rule(self.base_rule, level=0))

    def is_leaf(self, node):
        return node.populated() or isinstance(node, Constant)

    def execute(self, date=None):
        return self.base_rule.execute()

class NodeFactory(object):
    @staticmethod
    def create_node(node_type, **kwargs):
        node_type = node_type.lower().replace(" ", "")
        try:
            return NODE_TYPES[node_type](**kwargs)
        except Exception as e:
            print(e)
            return None