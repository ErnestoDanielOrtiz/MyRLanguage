from lark import Visitor
from VariableTable import VariableTable
from Variable import Variable
from Cuadruplos import Cuadruplos
from SemanticCube import SemanticCube

varTable = VariableTable()
quads = Cuadruplos()
semCube = SemanticCube()

pilaSaltos = []
pilaTipo = []
pilaOperadores = []
pilaOperandos = []
pilaVariables = []

nVarTemp = 0

contadores = []

class NeuralgicPoints(Visitor):

    def start(self, tree):
        pilaSaltos.append(quads.contador)
        quads.addCuadruplo("GOTO-MAIN", None, None, "N/A")

    def np_main(self, tree):
        quads.fillCuadruplo(pilaSaltos.pop(), quads.contador)
