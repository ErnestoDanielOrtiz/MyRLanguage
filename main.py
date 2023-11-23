from lark import Lark
from lark import Visitor
from NeuralgicPoints import NeuralgicPoints
from SemanticCube import SemanticCube
from myR import *

test = 'factorialIterativo.txt'


parser = Lark(open("grammar.g", 'r').read()) 
result = ''

def compile():
    input = open(test, 'r').read()
    result = parser.parse(input)
    # write tree to file
    with open('tree.txt', 'w') as f:
        resultPretty = parser.parse(input).pretty()
        f.write(str(resultPretty))

    execute(result)


def execute(result):
    NeuralgicPoints().visit_topdown(result)
    virtualMachine()
    
def main():
    compile()

if __name__ == '__main__':
    main()
