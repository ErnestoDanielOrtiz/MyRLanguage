class VirtualMemory():

    def __init__(self):
        self.memory = {
            'global' : {
                'int' : 1000,
                'float' : 3000,
                'string' : 5000,
                'bool' : 7000
            },
            'local' : {
                'int' : 10000,
                'float' : 13000,
                'string' : 15000,
                'bool' : 17000
            },
            'const' : {
                'int' : 20000,
                'float' : 230000,
                'string' : 25000,
                'bool' : 27000
            },
            'temporal' : {
                'int' : 30000,
                'float' : 33000,
                'string' : 36000,
                'bool' : 39000,
                'pointer': 42000
            }
        }

        self.virtualMemory = {}

        #Globales
        self.intGlobal = 1000
        self.floatGlobal = 3000
        self.stringGlobal = 5000
        self.boolGlobal = 7000

        #Locales
        self.intLocal = 10000
        self.floatLocal = 13000
        self.stringLocal = 15000
        self.boolLocal = 17000

        #Constantes
        self.intC = 20000
        self.floatC = 23000
        self.stringC = 25000
        self.boolC = 27000

        #Temporales
        self.intTemporal = 30000
        self.floatTemporal = 33000
        self.stringTemporal = 36000
        self.boolTemporal = 39000
        self.pointerTemporal = 42000
    
    def __str__(self):
        return str(self.memory)