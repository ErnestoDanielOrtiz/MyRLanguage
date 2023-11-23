class FunctionDirectory():
    
    def __init__(self):
        self.funcDir = {}
    
    def doesExist(self, func):
        if func.name in self.funcDir:
            return True
        else:
            return False
    
    def addFunction(self, func):
        if not self.doesExist(func):
            self.funcDir[func.name] = func
    
    def getFunction(self, funcName):
        if funcName in self.funcDir:
            return self.funcDir[funcName]
        else:
            return None

    def updateFunction(self, func):
        if self.doesExist(func):
            self.funcDir[func.name] = func
        else:
            print("Function ", func.name, " does not exist in directory")
    
    def printDirecctory(self):
        for func in self.funcDir:
            print(self.funcDir[func].name)
            self.funcDir[func].printFunction()

    def __str__(self):
        return str(self.funcDir)