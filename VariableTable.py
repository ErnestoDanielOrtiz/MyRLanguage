class VariableTable:

    #Inicializa la tabla de variables
    def __init__ (self):
        self.variables = {}

    #Busca si existe la variable en la tabla
    def doesExist(self, var):
        if var.name in self.variables:
            return True
        else:
            return False
    
    #Agrega variables a la tabla
    def addVariable(self, var):
        if not self.doesExist(var):
            self.variables[var.name] = var
    
    #Busca una variable en la tabla
    def getVar(self, varName):
        if varName in self.variables:
            return self.variables[varName]
        else:
            return None