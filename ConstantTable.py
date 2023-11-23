class ConstantTable():

    def __init__(self):
        self.table = []

    def addConstant(self, dirV, constant, type):
        self.table.append([dirV, constant, type])

    def getConstant(self, dirV):
        for constant in self.table:
            if constant[0] == dirV:
                return constant[1]
        return None
    
    def getDirV(self, const):
        for constant in self.table:
            if str(constant[1]) == str(const):
                return constant[0]
        return None
    
    def doesExist(self, const):
        for constant in self.table:
            if str(constant[1]) == str(const):
                return True
        return False

    def writeTable(self):
        with open('Constantes.txt', 'w') as f:
            for constant in self.table:
                f.write(str(constant) + '\n')
    
    def __str__(self):
        return str(self.table)