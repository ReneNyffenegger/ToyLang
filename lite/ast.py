from re import L
from rply.token import BaseBox
import random
import sys
import pdb


class BinaryOp(BaseBox):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Add(BinaryOp):
    def eval(self):
        return self.left.eval() + self.right.eval()


class Sub(BinaryOp):
    def eval(self):
        return self.left.eval() - self.right.eval()


class Mul(BinaryOp):
    def eval(self):
        return self.left.eval() * self.right.eval()


class Div(BinaryOp):
    def eval(self):
        return self.left.eval() / self.right.eval()


class Print():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value.eval()


class Integer():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return int(self.value)


class Input():
    def __init__(self, value):
        self.value = value

    def eval(self):
        input(self.value.eval())
        return


class Newline():
    def eval(self):
        pass


class String():
    def __init__(self, value):
        self.value = str(value).strip('"')

    def eval(self):
        return str(self.value)


class Bool():
    def __init__(self, value):
        if value == "false":
            self.value = bool(value)
        if value == "true":
            self.value = bool(value)
        else:
            return ValueError(f"Invalid value {value}")

    def eval(self):
        return self.value


class Null():

    def eval(self):
        return self

    def to_string(self):
        return 'null'


class Comparison():
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        if self.left.eval() == self.right.eval():
            print("TRUE")
        else:
            print("FALSE")

    def if_eval(self):
        if self.left.eval() == self.right.eval():
            print("TRUE")
        else:
            print("FALSE")


class If():
    def __init__(self):
        print("INIT")

    def eval(self):
        print("Evaling")
        Comparison().eval()


class RandomInt():
    def __init__(self, range1, range2):
        self.range1 = int(range1)
        self.range2 = int(range2)

    def eval(self):
        return random.randint(self.range1, self.range2)


class Sum():
    def __init__(self, value):
        self.value = value

    def eval(self, value):
        return sum(value)
