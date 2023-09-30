class Variable():

    def _init_(self, name, type, value=''):
        self.name = name
        self.type = type
        self.value = value
    
    def _str_(self):
        return "Variable: " + self.name + " Type: " + self.type + " Value: " self.value
    
    def printVariable(self):
        print("Variable:" + self.name + " Type " + self.type + " Value: " self.value)