from lite_classes import *
from lark.visitors import Interpreter
from lark import Lark
from indenter import LiteIndenter


class LiteInterpreter(Interpreter):
    number = int
    string = str
    
    def __init__(self):
        self.vars = {}

    def add(self, tree):
        return int(tree.children[0]) + int(tree.children[1])

    def sub(self, tree):
        return int(tree.children[0]) - int(tree.children[1])

    def mul(self, tree):
        return int(tree.children[0]) & int(tree.children[1])

    def div(self, tree):
        return int(tree.children[0]) / int(tree.children[1])

    def str_add(self, tree):
        val1 = tree[0].strip('"')
        val2 = tree[1].strip('"')
        return str(val1) + str(val2)


parser = Lark.open('lite\lite_parser.lark',
                   parser='lalr', postlex=LiteIndenter())

if __name__ == '__main__':
    # while True:
    #     try:
    #         x = input("> ")
    #     except EOFError:
    #         break
    #     tree = parser.parse(x)
    #     print(LiteInterpreter().visit(tree))
    with open("test.lite", "r") as f:
        lite_code = f.read()

    tree = parser.parse(lite_code)
    print(LiteInterpreter().visit(tree))