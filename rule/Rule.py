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
from rule.computation.Divide import Divide


NODE_TYPES = {
    "greaterthan": GreaterThan,
    "lessthan": LessThan,
    "and": And,
    "equalto": Equals,
    "number": Number,
    "add": Add,
    "or": Or,
    "divide": Divide
}

class Rule():
    def __init__(self, raw_json, dates=[]):
        self.raw_json = raw_json
        self.base_rule = Base()
        self.base_rule.add_child(self.build(self.raw_json))
    
    def build(self, json):
        leaf_stack = []
        parent_stack = []
        node_index = 0
        while node_index < len(json):
            node = json[node_index]
            key = node[0]
            value = node[1]
            if key == "constant":
                node = NodeFactory.create_node("number", value=float(value))
                print(node_index, ", ", value)
            elif key != "parentheses":
                node = NodeFactory.create_node(value)
            else:
                if(value == "left"):
                    sub_rule = []
                    index = node_index + 1
                    while(json[index][1] != "right"):
                        sub_rule.append(json[index])
                        index += 1
                    node = self.build(sub_rule)
                    node_index = index
            if(self.is_leaf(node)):
                leaf_stack.append(node)
            else:
                parent_stack.append(node)
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
            leaf_stack = leaf_stack + unadded_leaves
            node_index += 1
            
        if not len(leaf_stack) == 1 and not len(parent_stack) == 0:
            print("Unable to configure rule")
        else:
            return leaf_stack.pop()
    
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