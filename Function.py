from Variable import Variable as v
from VariableTable import VariableTable as vt 

class Function:

    def __init__ (self, name, type, dirV, parameters=[], variables={}, intTemp = 0, floatTemp = 0, booleanTemp = 0, stringTemp = 0, intVar = 0, floatVar = 0, booleanVar = 0, stringVar = 0, pointerTemp = 0):
        self.name = name
        self.type = type
        self.dirV = dirV
        self.parameters = parameters
        self.variables = variables
        self.intTemp = intTemp
        self.floatTemp = floatTemp
        self.booleanTemp = booleanTemp
        self.stringTemp = stringTemp
        self.intVar = intVar
        self.floatVar = floatVar
        self.booleanVar = booleanVar
        self.stringVar = stringVar
        self.pointerTemp = pointerTemp
    
    def addParameters(self, parameter, type):
        variable = v.Variable(parameter, type)
        self.variables.addVariable(variable)

    def addVariable(self, v):
        self.variables.addVariable(v)
    
    def getFunction(self, funcName):
        if funcName in self.functions:
            return self.functions[funcName]
        else:
            return None
    
    def updateFunction(self, func):
        if self.doesExist(func.name):
            self.functions[func.name] = func
        else:
            print("Function ", func.name, "does not exist in directory")
    
    def printFunction(self):
        print("Function: " + self.namme + " Type: " + self.type + " DirV: " + str(self.dirV))
        print("Parameters: ")
        for parameter in self.parameters:
            print(parameter)
        print("Variables: ")
        for v in self.variables:
            print(v)
    
    def __str__(self):
        return str(self.name) + " : " + str(self.type) + " (" + str(self.parameters) + " " + str(self.dirV) + " " + str(self.variables) + " " + str(self.intTemp) + " " + str(self.floatTemp) + " " + str(self.booleanTemp) + " " + str(self.stringTemp) + " " + str(self.intVar) + " " + str(self.floatVar) + " " + str(self.booleanVar) + " " + str(self.stringVar) + " )"
