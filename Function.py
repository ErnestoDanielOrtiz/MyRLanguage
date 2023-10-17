import Variable as v
import VariableTable as vt 

class Function:

    def __init__ (self, name, type, parameters=[]):
        self.name = name
        self.type = type
        self.parameters = parameters
        self.variables = vt.VariableTable
    
    def addParameters(self, parameter, type):
        variable = v.Variable(parameter, type)
        self.variables.addVariable(variable)

    def addVariable(self, v):
        self.variables.addVariable(v)
    
