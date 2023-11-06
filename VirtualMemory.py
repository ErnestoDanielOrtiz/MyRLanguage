class Memory():

    def __init__(self):
        self.memory = {
            'global' : {
                'int' : 1000,
                'float' : 2000,
                'string' : 3000,
                'bool' : 4000
            },
            'local' : {
                'int' : 5000,
                'float' : 6000,
                'string' : 7000,
                'bool' : 8000
            },
            'const' : {
                'int' : 9000,
                'float' : 10000,
                'string' : 11000,
                'bool' : 12000
            },
            'temp' : {
                'int' : 13000,
                'float' : 14000,
                'string' : 15000,
                'bool' : 16000
            }
        }

        self.virtualMemory = {}

        #Globales
        self.intG = 1000
        self.floatG = 2000
        self.stringG = 3000
        self.boolG = 4000

        #Locales
        self.intL = 5000
        self.floatL = 6000
        self.stringL = 7000
        self.boolL = 8000

        #Constantes
        self.intC = 9000
        self.floatC = 10000
        self.stringC = 11000
        self.boolC = 12000

        #Temporales
        self.intT = 13000
        self.floatT = 14000
        self.stringT = 15000
        self.boolT = 16000
    
    def __str__(self):
        return str(self.memory)