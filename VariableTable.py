class VariableTable:

    #Inicializa la tabla de variables
    def __init__ (self):
        self.variables = {}
        self.globales = {}

    #Busca si existe la variable en la tabla
    def doesExist(self, var):
        if var in self.variables:
            return True
        else:
            return False
    
    def doesExistGlobal(self, var):
        if var in self.globales:
            return True
        else:
            return False
    
    #Agrega variables a la tabla
    def addVariable(self, var):
        if not self.doesExist(var.name):
            self.variables[var.name] = var

    def addVariableGlobal(self, var):
        if not self.doesExistGlobal(var.name):
            self.globales[var.name] = var
    
    def updateVariable(self, var):
        if self.doesExist(var.name):
            self.variables[var.name] = var
        else:
            print("Variable ", var.name, " does not exist in directory")
    
    def updateVariableGlobal(self, var):
        if self.doesExistGlobal(var.name):
            self.globales[var.name] = var
        else:
            print("Variable ", var.name, " does not exist in directory")
    
    #Busca una variable en la tabla
    def getVariable(self, varName):
        if varName in self.variables:
            return self.variables[varName]
        else:
            return None

    def getVariableGlobal(self, varName):
        if varName in self.globales:
            return self.globales[varName]
        else:
            return None

    def getVariableGlobalID(self, id):
        for var in self.globales:
            if self.globales[var].dirV == id:
                return self.globales[var]
        return None

    def printTable(self):
        for var in self.variables:
            var.printVariable()
    
    def printTableGlobal(self):
        for var in self.globales:
            var.printVariable()

    def resetTable(self):
        self.variables = {}
    
    def resetTableGlobal(self):
        self.globales = {}

    def __str__(self):
        string = ""
        for var in self.variables:
            string += str(self.variables[var]) + "\n"
        return string

    def printGlobales(self):
        string = ""
        for var in self.globales:
            string += str(self.globales[var]) + "\n"
        print(string)