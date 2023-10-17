class FunctionDirectory():
    
    def __init__(self):
        self.funcDir = {}
    
    def doesExist(self, function):
        if function.name in self.funcDir:
            return True
        else:
            return False
    
    def addFunction(self, function):
        if not self.doesExist(function):
            self.funcDir[function.name] = function
    
    def getFunction(self, funcName):
        if funcName in self.funcDir:
            return self.funcDir[funcName]
        else:
            return None