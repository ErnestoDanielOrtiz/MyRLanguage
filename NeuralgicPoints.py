from lark import Token, Visitor
from VariableTable import VariableTable
from Variable import Variable
from Cuadruplos import Cuadruplos
from SemanticCube import SemanticCube
from Function import Function
from FunctionDirectory import FunctionDirectory
from ConstantTable import ConstantTable
from VirtualMemory import VirtualMemory

funcDir = FunctionDirectory()
constTable = ConstantTable()
varTable = VariableTable()
cuadruplos = Cuadruplos()
semCube = SemanticCube()
memory = VirtualMemory()

pilaSaltos = []
pilaTipo = []
pilaOperadores = []
pilaOperandos = []
pilaVariables = []
pilaFor = []
pilaContadores = []
pilaResultadosFunciones = []
pilaContexto = ["global"]
pilaRevisarVar = []

global VC, VF, contVarsTemp, contadores

funcVars = 0
VC = -1
VF = -1
contFor = 0
contVarsTemp = 0

contadores = []

pilaTempInt = []
pilaTempFloat = []
pilaTempString = []
pilaTempBool = []
contInt = 0
contFloat = 0
contString = 0
contBool = 0
contTempInt = 0
contTempFloat = 0
contTempString = 0
contTempBool = 0
contIntVars = 0
contFloatVars = 0
contStringVars = 0
contBoolVars = 0
contPointers = 0

isRecursive = False
newRecursive = True
recursiveGOTO = -1

class NeuralgicPoints(Visitor):

    def np_main(self, tree):
        pilaSaltos.append(cuadruplos.contador)
        cuadruplos.addCuadruplo("GOTO-MAIN", None, None, "N/A")
        cuadruplos.fillCuadruplo(pilaSaltos.pop(), cuadruplos.contador)

        #Resetea el valor de variables locales
        global contVarsTemp, contTempInt, contTempFloat, contTempString, contTempBool, contIntVars, contFloatVars, contStringVars, contBoolVars, contPointers
        contVarsTemp = 1
        memory.intLocal = memory.memory["local"]["int"]
        memory.floatLocal = memory.memory["local"]["float"]
        memory.stringLocal = memory.memory["local"]["string"]
        memory.booleanLocal = memory.memory["local"]["boolean"]
        memory.intTemporal = memory.memory["temporal"]["int"]
        memory.floatTemporal = memory.memory["temporal"]["float"]
        memory.stringTemporal = memory.memory["temporal"]["string"]
        memory.booleanTemporal = memory.memory["temporal"]["boolean"]
        memory.pointerTemporal = memory.memory["temporal"]["pointer"]
        contTempInt = 0
        contTempFloat = 0
        contTempString = 0
        contTempBool = 0
        contIntVars = 0
        contFloatVars = 0
        contStringVars = 0
        contBoolVars = 0
        contPointers = 0

        funcMain = Function("main", "void", cuadruplos.contador, [])
        funcDir.addFunction(funcMain)

    #Declarar variables globales en la tabla de variables
    def simpleglobal(self, tree):
        varName = tree.children[1].value
        varType = tree.children[3].children[0].value
        varEqual = tree.children[4].value
        varValue = 0
        dirV = -1

        if (varEqual == "="):
            varValue = -1
        else:
            varValue = "N/A"

        if varType == 'int':
            dirV = memory.intGlobal
            memory.intGlobal += 1
        elif varType == 'float':
            dirV = memory.floatGlobal
            memory.floatGlobal += 1
        elif varType == 'string':
            dirV = memory.stringGlobal
            memory.stringGlobal += 1
        elif varType == 'boolean':
            dirV = memory.booleanGlobal
            memory.booleanGlobal += 1
        
        varTable.addVariableGlobal(Variable(varName, varType, varValue, dirV))
        varTable.addVariable(Variable(varName, varType, varValue, dirV))
        pilaVariables.append(varName)
    
    #Declarar arreglos globales en la tabla de variables
    def compuestoglobal(self, tree):
        x = 1

    def arreglo(self, tree):

        if len(pilaOperandos) < 1:
            global contInt, contPointers
            arrID = tree.children[0].value
            indexDirV = -1
            arrDirV = -1
            arrSizeDirV = -1
            valueDirV = -1
            indexR = -1
            arrType = -1
            arrDirV = varTable.getVariable(arrID)

            if arrDirV == None:
                print("Error: Variable " + arrID + " not defined")
                exit()

            arrType = arrDirV.type
            arrSize = int(arrDirV.size)
            arrSizeDirV = constTable.getDirV(arrSize)

            if arrSizeDirV == None:
                dirV = memory.memory["constante"]["int"] + contInt
                contInt += 1
                constTable.addConstant(dirV, arrSize, "int")
                arrSizeDirV = dirV
            
            arrDirV = arrDirV.dirV
            #Aqui ya se tiene la direcccion del arreglo y el size

            try:
                arrIndex = int(tree.children[2].value)
                constExist = constTable.getDirV[arrIndex]

                if constExist == None:
                    dirV = memory.memory["constante"]["int"] + contInt
                    contInt += 1
                    constTable.addConstant(dirV, arrIndex, "int")
                    indexDirV = dirV

                else:
                    indexDirV = constExist
                    #Aqui ya se tiene la direccion de memoria del index

            except:
                arrIndex = tree.children[2].value
                indexDirV = varTable.getVariable(arrIndex)

                if indexDirV == None:
                    print("Error: Variable " + arrIndex + " not defined")
                    exit()

                indexDirV = indexDirV.dirV
                valueDirV = varTable.getVariable(arrIndex)
                #Aqui ya se tiene la direccion de memoria del index

            cuadruplos.addCuadruplo("VER", indexDirV, 0, arrSizeDirV)
            pilaDirV = memory.pointerTemporal
            memory.pointerTemporal += 1
            contPointers += 1
            cuadruplos.addCuadruplo("+A", indexDirV, arrDirV, pilaDirV)
            pilaVariables.append(pilaDirV)
            pilaVariables.append(arrID)
            pilaTipo.append(arrType)
        else: 
            indexDirV = -1
            arrDirV = -1
            arrSize = -1
            arrSizeDirV = -1
            arrID = tree.children[0].value
            arrVar = varTable.getVariable(arrID)

            if arrVar == None:
                print("Error: Variable " + arrID + " not defined")
                exit()
            arrType = arrVar.type
            arrSize = int(arrVar.size)
            arrSizeDirV = constTable.getDirV(arrSize)

            if arrSizeDirV == None:
                dirV = memory.memory["constante"]["int"] + contInt
                contInt += 1
                constTable.addConstant(dirV, arrSize, "int")
                arrSizeDirV = dirV
            
            arrDirV = arrVar.dirV
            #Aqui ya se tiene la direcion y el size del arreglo

            try:
                arrIndex = int(tree.children[2].value)
                constExist = constTable.getDirV(arrIndex)
                
                if constExist == None:
                    dirV = memory.memory["constante"]["int"] + contInt
                    contInt += 1
                    constTable.addConstant(dirV, arrIndex, "int")
                    indexDirV = dirV
                else:
                    indexDirV = constExist
                    #Aqui ya se tiene la direccion del index
            
            except:
                arrIndex = tree.children[2].value
                indexDirV = varTable.getVariable(arrIndex)

                if indexDirV == None:
                    print("Error: Variable " + arrIndex + " not defined")
                    exit()

                indexDirV = indexDirV.dirV
                valueDirV = varTable.getVariable(arrIndex)
                #Aqui ya se tiene la direccion del index
            
            cuadruplos.addCuadruplo("VER", indexDirV, 0, arrSizeDirV)
            pilaDirV = memory.pointerTemporal
            memory.pointerTemporal += 1
            contPointers += 1
            cuadruplos.addCuadruplo("+A", indexDirV, arrDirV, pilaDirV)
            pilaVariables.append(pilaDirV)
            pilaVariables.append(arrID)
            pilaTipo.append(arrType)
            cuadruplos.writeCuadruplos()
    
    #Declarar variables en la tabla de variables
    def simpledeclaration(self, tree):
        
        global contIntVars, contFloatVars, contStringVars, contBoolVars

        varName = tree.children[1].value
        varType = tree.children[4].children[0].value

        if varType == 'int':
            dirV = memory.intLocal
            memory.intLocal += 1
            contIntVars += 1
        elif varType == 'float':
            dirV = memory.floatLocal
            memory.floatLocal += 1
            contFloatVars += 1
        elif varType == 'string':
            dirV = memory.stringLocal
            memory.stringLocal += 1
            contStringVars += 1
        elif varType == 'boolean':
            dirV = memory.booleanLocal
            memory.booleanLocal += 1
            contBoolVars += 1
        
        varTable.addVariable(Variable(varName, varType, "N/A", dirV))

    #Declarar variables en la tabla de variables y asignarles valor
    def simpleasignacion(self, tree):

        global contIntVars, contFloatVars, contStringVars, contBoolVars

        varName = tree.children[1].value
        pilaVariables.append(varName)
        varType = tree.children[4].children[0].value
        varValue = "N/A"

        if varType == 'int':
            dirV = memory.intLocal
            memory.intLocal += 1
            contIntVars += 1
        elif varType == 'float':
            dirV = memory.floatLocal
            memory.FloatLocal += 1
            contfloatVars += 1
        elif varType == 'string':
            dirV = memory.stringLocal
            memory.stringLocal += 1
            contStringVars += 1
        elif varType == 'boolean':
            dirV = memory.booleanLocal
            memory.booleanLocal += 1
            contBoolVars += 1
        
        varTable.addVariable(Variable(varName, varType, varValue, dirV))

    #Declarar arreglos
    def compuestadeclaracion(self, tree):

        global contIntVars, contFloatVars, contStringVars, contBoolVars

        varName = tree.children[1].value
        varSize = tree.children[3].value
        varType = tree.children[6].children[0].value

        if varType == 'int':
            dirV = memory.intLocal
            memory.intLocal += int(varSize)
            contIntVars += int(varSize)
        elif varType == 'float':
            dirV = memory.floatLocal
            memory.floatLocal += int(varSize)
            contFloatVars += int(varSize)
        elif varType == 'string':
            dirV = memory.stringLocal
            memory.stringLocal += int(varSize)
            contStringVars += int(varSize)
        elif varType == 'boolean':
            dirV = memory.booleanLocal
            memory.booleanLocal += int(varSize)
            contBoolVars += int(varSize)
        
        varTable.addVariable(Variable(varName, varType, "N/A", dirV, "local", varSize))

    #Declarar arreglos y asignarles valor
    def compuestaasignacion(self, tree):
        varName = tree.children[1].value
        varSize = tree.children[3].value
        varType = tree.children[6].children[0].value
        varTable.addVariable(Variable(varName, varType, "N/A"))

    #Asignar valor a una variable
    def asignacionsimple(self, tree):
        varName = tree.children[0].value
        pilaVariables.append(varName)
        var = varTable.getVariable(varName)
        
        if var == None:
            print("Error: variable not defined")
            exit()
    
    #Asignar valor a un arreglo
    def asignacioncompleja(self, tree):
        varName = tree.children[0].value
        varIndex = -1
        arrDirV = -1
        valDirV = -1
        varIndex = tree.children[2].value
        pilaVariables.append(varName)
        pilaVariables.append(varIndex)

    #Cuadruplos de arerglo
    def np_arr(self, tree):
        
        global contInt, contPointers
        
        index = pilaVariables.pop()
        arr = pilaVariables.pop()
        indexR = -1
        indexDirV = -1
        arrDirV = -1
        valueDirV = -1
        arrSize = -1
        arrSizeDirV = -1

        arrDirV = varTable.getVariable(arr)

        if arrDirV == None:
            print("Error: Variable" + arr + " not defined")
            exit()
        
        arrSize = int(arrDirV.size)
        arrSizeDirV = constTable.getDirV(arrSize)

        if arrSizeDirV == None:
            dirV = memory.memory["constante"]["int"] + contInt
            contInt += 1
            constTable.addConstant(dirV, arrSize, "int")
            arrSizeDirV = dirV
        
        arrDirV = arrDirV.dirV
        #Ya se tiene la direccion del arreglo y su size

        try:
            indexR = int(index)
            valueDirV = constTable.getDirV(indexR)
            
            if valueDirV == None:
                dirV = memory.memory["constante"]["int"] + contInt
                contInt += 1
                constTable.addConstant(dirV, indexR, "int")
                indexDirV = dirV
            else:
                indexDirV = constTable.getDirV(indexR)
        except:
            indexR = index
            indexDirV = varTable.getVariable(indexR)

            if indexDirV == None:
                print("Error: Variable", indexR, "not defined")
                exit()
            
            indexDirV = indexDirV.dirV
            valueDirV = varTable.getVariable(index)
            #Ya se tiene la direccion del index
        
        cuadruplos.addCuadruplo("VER", indexDirV, 0, arrSizeDirV)
        pilaDirV = memory.pointerTemporal
        memory.pointerTemporal += 1
        contPointers += 1
        cuadruplos.addCuadruplo("+A", indexDirV, arrDirV, pilaDirV)
        pilaVariables.append(pilaDirV)
        pilaVariables.append(arr)

    #Cuadruplos de IF
    #Agrega el GotoF
    def np_if(self, tree):
        result = pilaOperandos.pop()
        pilaTipo.pop()
        pilaSaltos.append(cuadruplos.contador)
        cuadruplos.addCuadruplo("GOTOF", result, None, "N/A")
    
    #Llenar cuadruplo de salto falso
    def np_if_2(self, tree):
        cuadruplos.fillCuadruplo(pilaSaltos.pop(), cuadruplos.contador)

    #Crear cuadruplo Goto
    def np_if_3(self, tree):
        cuadruplos.fillCuadruplo(pilaSaltos.pop(), cuadruplos.contador + 1)
        pilaSaltos.append(cuadruplos.contador)
        cuadruplos.addCuadruplo("GOTO", None, None, "N/A")

    #Cuadruplos For
    #Agregar True a la pila de for anidados
    def np_for(self, tree):
        pilaFor.append(True)

    #Maneja la asignacion de la variable del for
    def asignacionfor(self, tree):
        global contIntVars
        varName = tree.children[0].value
        pilaVariables.append(varName)
        dirV = memory.intLocal
        memory.intLocal += 1
        contIntVars += 1
        varTable.addVariable(Variable(varName, "int", 'N/A', dirV))
    
    #Igualar la variable del for y VC
    def np_for_false(self, tree):
        global contFor, contIntVars
        result = pilaOperandos.pop()
        varName = pilaVariables.pop()
        varType = pilaTipo.pop()
        contFor += 1
        varNameDir = varTable.getVariable(varName).dirV
        cuadruplos.addCuadruplo("=", result, None, varNameDir)
        dirV = memory.intLocal
        memory.intLocal += 1
        contIntVars += 1
        varTable.addVariable(Variable("VC" + str(contFor-1), "int", "N/A", dirV))
        cuadruplos.addCuadruplo("=", varNameDir, None, dirV)

    #Guardar el contador del for y los fors anidados
    def contador(self, tree):
        varName = tree.children[0].children[0].value
        operator = tree.children[0].children[1].children[0].value
        cont = 1
        
        if operator == "+=" or operator == "-=" or operator == "*=" or operator == "/=":
            cont = tree.children[0].children[2].value
        
        pilaContadores.append([varName, operator, cont])

    #Cuadruplo de for
    def np_for_2(self, tree):
        global contVarsTemp, contFor, contInt, contIntVars, contTempInt
        pilaContador = pilaContadores.pop()
        temp = memory.intTemporal
        memory.intTemporal += 1
        dirVC = varTable.getVariable("VC" + str(contFor-1)).dirV
        cont = -1
        exist = constTable.doesExist(int(pilaContador[2]))

        if exist == False:
            dirV = memory.memory["constante"]["int"] + contInt
            contInt += 1
            constTable.addConstant(dirV, int(pilaContador[2]), "int")
            cont = dirV 
        else:
            cont = constTable.getDirV(int(pilaContador[2]))

        cuadruplos.addCuadruplo(pilaContador[1], dirVC, cont, temp)
        contVarsTemp += 1
        cuadruplos.addCuadruplo("=", temp, None, dirVC)
        contTempInt += 1
        dirContador = varTable.getVariable(pilaContador[0]).dirV
        cuadruplos.addCuadruplo("=", temp, None, dirContador)
        contTempInt += 1
        fill = pilaSaltos.pop()
        add = pilaSaltos.pop()
        cuadruplos.addCuadruplo("GOTO", None, None, add)
        cuadruplos.fillCuadruplo(fill, cuadruplos.contador)

    #Cuadruplos de while
    def np_while(self, tree):
        result = pilaOperandos.pop()
        pilaTipo.pop()
        pilaSaltos.append(cuadruplos.contador)
        cuadruplos.addCuadruplo("GOTOF", result, None, "N/A")

    #Llenar cuadruplo de while y Goto
    def np_while_2(self, tree):
        fill = pilaSaltos.pop()
        add = pilaSaltos.pop()
        cuadruplos.addCuadruplo("GOTO", None, None, add)
        cuadruplos.fillCuadruplo(fill, cuadruplos.contador)

    #Agregar salto a la pila
    def np_while_3(self, tree):
        pilaSaltos.append(cuadruplos.contador)
    
    #Funciones
    def funcion(self,tree):

        global contVarsTemp
        contVarsTemp = 1

        #Resetea los contadores de variables y temporales
        memory.intLocal = memory.memory["local"]["int"]
        memory.floatLocal =  memory.memory["local"]["float"]
        memory.stringLocal = memory.memory["local"]["string"]
        memory.booleanLocal = memory.memory["local"]["bool"]
        memory.intTemporal = memory.memory["temporal"]["int"]
        memory.floatTemporal = memory.memory["temporal"]["float"]
        memory.stringTemporal = memory.memory["temporal"]["string"]
        memory.booleanTemporal = memory.memory["temporal"]["bool"]
        
        varName = tree.children[1].value
        pilaContexto.append(varName)
        funcType = tree.children[7].children[0].value
        pilaOperandos.append(varName)
        pilaTipo.append(funcType)
        vars = tree.children[4].scan_values(lambda v: isinstance(v, Token))
        dirFuncVar = -1

        #Agrega la variable global con tipo de la funcion
        if funcType == "int":
            dirFuncVar = memory.intGlobal
            memory.intGlobal += 1
        elif funcType == "float":
            dirFuncVar = memory.floatGlobal
            memory.floatGlobal += 1
        elif funcType == "string":
            dirFuncVar = memory.stringGlobal
            memory.stringGlobal += 1
        elif funcType == "boolean":
            dirFuncVar = memory.booleanGlobal
            memory.booleanGlobal += 1

        varTable.addVariableGlobal(Variable(varName, funcType, "N/A", dirFuncVar))

        global funcVars
        
        for var in vars:
            if var == "int" or var == "float" or var == "string" or var == "boolean":
                pilaTipo.append(var.value)
            elif var == ',' or var == ':':
                pass
            else:
                pilaOperandos.append(var.value)
                funcVars +=1

    #Void
    def funcionvoid(self,tree):
        funcName = tree.children[1].value
        funcType = tree.children[7].value
        pilaOperandos.append(funcName)
        pilaTipo.append(funcType)
        pilaContexto.append(funcName)
        vars = tree.children[4].scan_values(lambda v: isinstance(v, Token))
        global funcVars
        for var in vars:
            if var == "int" or var == "float" or var == "string" or var == "boolean":
                pilaTipo.append(var.value)
            elif var == ',' or var == ':':
                pass
            else:
                pilaOperandos.append(var.value)
                funcVars +=1

    #Agregar funcion al directorio
    def np_func_id(self,tree):
        global funcVars, contIntVars, contFloatVars, contStringVars, contBoolVars
        params = []
        pilaOperandos.reverse()
        pilaTipo.reverse()
        funcName = pilaOperandos.pop()
        funcType = pilaTipo.pop()
        dirV = -1

        for i in range(funcVars):
            varType = pilaTipo.pop()
            if varType == 'int':
                dirV = memory.intLocal
                memory.intLocal += 1
                contIntVars += 1
            elif varType == 'float':
                dirV = memory.floatLocal
                memory.floatLocal += 1
                contFloatVars += 1
            elif varType == 'string':
                dirV = memory.stringLocal
                memory.stringLocal += 1
                contStringVars += 1
            elif varType == 'boolean':
                dirV = memory.booleanLocal
                memory.booleanLocal += 1
                contBoolVars += 1
            
            varName = pilaOperandos.pop()
            varTable.addVariable(Variable(varName, varType, "N/A", dirV, "local"))
            params.append([ varName, varType])

        funcVars = 0
        func = Function(funcName, funcType, cuadruplos.contador, params) 
        funcDir.addFunction(func)

    #Agregar restultado de una funcion a la tabla de variables
    def np_func_result(self,tree):
        global funcVars, isRecursive, recursiveGOTO, newRecursive
        funcVars = 0
        exist = varTable.getVariable(pilaOperandos[-1])
        funcDirVGlobal = varTable.getVariableGlobal(pilaContexto[-1]).dirV        
        
        if exist != None:
            cuadruplos.addCuadruplo("RETURN", funcDirVGlobal, None, exist.dirV)
            if isRecursive and newRecursive:
                recursiveGOTO = cuadruplos.contador
                cuadruplos.addCuadruplo("GOTO", None, None, "N/A")
                newRecursive = False
        else:
            cuadruplos.addCuadruplo("RETURN", funcDirVGlobal, None, pilaOperandos[-1])
            if isRecursive and newRecursive:
                recursiveGOTO = cuadruplos.contador
                cuadruplos.addCuadruplo("GOTO", None, None, "N/A")
                newRecursive = False
        
        funcType = pilaTipo.pop()
        result = pilaOperandos.pop()
        value = "Get Result" 
        pResultFuncs.append([result, funcType, value])
    
    #Regresar valor
    def returnv(self,tree):
        global isRecursive
        isRecursive = True

    #Actualilzar contadores de variables y temporales
    def np_end_func(self, tree):
        global contVarsTemp, contTempInt, contIntVars, contInt, contFloatVars, contFloat, contBoolVars, contBool, contStringVars, contString, contTempFloat, contTempBool, contTempString, contPointers, isRecursive, recursiveGOTO
        if len(pilaRevisarVar) > 0:
            pilaRevisarVar.pop()

        contVInt = memory.intLocal - memory.memory["local"]["int"] 
        contVFloat = memory.floatLocal - memory.memory["local"]["float"] 
        contVString = memory.stringLocal - memory.memory["local"]["string"] 
        contVBoolean = memory.booleanLocal - memory.memory["local"]["boolean"] 
        contTInt = memory.intTemporal - memory.memory["temporal"]["int"]
        contTFloat = memory.floatTemporal - memory.memory["temporal"]["float"]
        contTString = memory.stringTemporal - memory.memory["temporal"]["string"]

        cuadruplos.addCuadruplo("ENDFUNC", None, None, None)

        if isRecursive:
            cuadruplos.fillCuadruplo(recursiveGOTO, cuadruplos.contador-1)
            isRecursive = False

        funcName = pilaContexto.pop()
        function = funcDir.getFunction(funcName)
        function.variables = varTable.variables
        function.intTemp = contTInt
        function.floatTemp = contTFloat
        function.stringTemp = contTString
        function.booleanTemp = contTString
        function.intVar = contVInt
        function.floatVar = contVFloat
        function.stringVar = contVString
        function.booleanVar = contVBoolean
        function.pointerTemp = contPointers
        funcDir.updateFunction(function)
        varTable.resetTable()
        
        contVarsTemp = 1
        memory.intLocal = memory.memory["local"]["int"]
        memory.floatLocal = memory.memory["local"]["float"]
        memory.stringLocal = memory.memory["local"]["string"]
        memory.booleanLocal = memory.memory["local"]["boolean"]
        memory.intTemporal = memory.memory["temporal"]["int"]
        memory.floatTemporal = memory.memory["temporal"]["float"]
        memory.stringTemporal = memory.memory["temporal"]["string"]
        memory.booleanTemporal = memory.memory["temporal"]["boolean"]
        memory.pointerTemporal = memory.memory["temporal"]["pointer"]
        contTempInt = 0
        contTempFloat = 0
        contTempString = 0
        contTempBool = 0
        contIntVars = 0
        contFloatVars = 0
        contStringVars = 0
        contBoolVars = 0
        contPointers = 0

    def llamadavoid(self, tree):
        global pilaVariables
        funcID = tree.children[0].value
        pilaVariables.append(funcID)

    def llamadafunc(self, tree):
        global pilaVariables
        funcID = tree.children[0].value
        pilaVariables.append(funcID)
    
    #Agrega cuadruplos de llamada a funciones
    def np_func_vars(self, tree):
        global pilaVariables, isRecursive
        funcName = pilaVariables.pop()
        funcVars = []
        
        for i in range(len(pilaOperandos)):
            funcVars.append([pilaOperandos.pop(), pilaTipo.pop()])

        funcVars.reverse()
        function = funcDir.getFunction(funcName)
        
        if len(funcVars) != len(function.params):
            print("Error: Incorrect number of parameters. Expected " + str(len(function.params)) + " parameters and  " + str(len(funcVars)) + " were received")
            exit()

        cuadruplos.addCuadruplo("ERA", None, None, function.name)

        for i in range(len(funcVars)):
            if funcVars[i][1] != function.params[i][1]:
                print("Error: Type mismatch. " + function.params[i][1] + " was expected " + funcVars[i][1] + " was received")
                exit()
            exist = varTable.getVariable(funcVars[i][0])
            cuadruplos.writeCuadruplos()
            
            #Agrega variables en caso de recursion
            if(len(function.variables)) == 0:
                function.variables = varTable.variables
                funcDir.updateFunction(function)
                isRecursive = True
                
            varDir = function.variables[function.params[i][0]].dirV

            if exist != None:
                cuadruplos.addCuadruplo("PARAM", exist.dirV, None, varDir)
            else:
                cuadruplos.addCuadruplo("PARAM", funcVars[i][0], None, varDir)

        cuadruplos.addCuadruplo("GOSUB", None, None, function.dirV)

        if function.type != "void":
            global contTempInt, contTempFloat, contTempString, contTempBool
            dirGlobal = varTable.getVariableGlobal(function.name).dirV
            temp = -1

            if function.type == "int":
                temp = memory.intTemporal
                memory.intTemporal += 1
                contTempInt += 1
                pilaTipo.append("int")
            elif function.type == "float":
                temp = memory.floatTemporal
                memory.floatTemporal += 1
                contTempFloat += 1
                pilaTipo.append("float")
            elif function.type == "string":
                temp = memory.stringTemporal
                memory.stringTemporal += 1
                contTempString += 1
                pilaTipo.append("string")
            elif function.type == "boolean":
                temp = memory.booleanTemporal
                memory.booleanTemporal += 1
                contTempBool += 1
                pilaTipo.append("boolean")
            cuadruplos.addCuadruplo("=", dirGlobal, None, temp)
            pilaOperandos.append(temp)

    #Leer
    def read(self,tree):
        varID = tree.children[2].value
        exist = varTable.getVariable(varID)
        if exist == None:
            print("Error: Variable " + varID + " undefined")
            exit()
        varType = exist.type
        cuadruplos.addCuadruplo("READ", None, None, exist.dirV)

    #Escribir
    def escritura(self, tree):
        arrID = -1
        index = -1
        try:
            arrID = tree.children[2].children[0].value
            try:
                index = int(tree.children[2].children[2].value)
                var = varTable.getVariable(arrID)
                indexID = var.dirV
                if var == None:
                    print("Error: Variable " + arrID + " not defined")
                    exit()

                if var.type != "int":
                    print("Error: Array index must be int")
                    exit()

                varSize = int(var.size)
                if index >= varSize:
                    print("Error: Out of bounds")
                    exit()

                dirV = indexID + index
                pilaOperandos.append(dirV)
                pilaTipo.append(var.type)
            except:
                index = tree.children[2].children[2].value
                var = varTable.getVariable(index)
                array = varTable.getVariable(arrID)
                arrSize = int(array.size)
                index = -1
                if var.value >= 20000 and var.value < 29000:
                    index = constTable.getConstante(var.value)
                    dirV = array.dirV + index

                    if var == None:
                        print("Error: Variable " + index + " not defined")
                        exit()

                    if var.type != "int":
                        print("Error: Array index must be int")
                        exit()

                    varSize = int(var.size)
                    if int(index) >= arrSize:
                        print("Error: Out of bounds")
                        exit()

                    pilaOperandos.append(dirV)
                    pilaTipo.append(var.type)
                else:
                    index = var.value
                    dirV = index
                    varSize = int(var.size)
                    pilaOperandos.append(dirV)
                    pilaTipo.append(var.type)
                
        except:
            pass

    def np_escritura(self, tree):

        if len(pilaOperandos) == 0:
            x = 0
        else:
            value = pilaOperandos.pop()
            pilaTipo.pop()
            exist = varTable.getVariable(value)
            dirV = -1
            if exist != None:
                if exist.value == "N/A":
                    dirV = exist.dirV
                elif exist.value >= 42000:
                    dirV = exist.value
                else:
                    dirV = exist.dirV
            else:
                dirV = value
            cuadruplos.addCuadruplo("PRINT", None, None, dirV)

    #Agregar suma o resta a la pila de operadores
    def expy(self, tree):
        pilaOperadores.append(tree.children[0].value)

    #Agregar multiplicacion o division a la pila de operadores
    def terminoy(self, tree):
        pilaOperadores.append(tree.children[0].value)

    #Agregar simbolos de logica a la pila de operadores
    def np_logico(self, tree):
        pilaOperadores.append(tree.children[0].value)

    #Cuadruplos logicos
    def np_logico_2(self, tree):

        global contVarsTemp, contTempBool
        cuadruplos.writeCuadruplos

        if len(pilaOperadores) > 0:

            if len(pilaVariables) == 2:
                pilaVariables.pop()
                right_operand = pilaVariables.pop()
                left_operand = pilaOperandos.pop()
                operator = pilaOperadores.pop()
                right_type = pilaTipo.pop()
                left_type = pilaTipo.pop()
                result_type = semCube.getValue(operator,left_type, right_type)

                if result_type == "error":
                    print("Error: Type mismatch")
                    exit()

                temp = memory.booleanTemporal
                existLeft = varTable.getVariable(left_operand)

                if existLeft != None:
                    left_operand = existLeft.dirV

                cuadruplos.addCuadruplo(operator + 'A', left_operand, right_operand, temp)
                memory.booleanTemporal += 1
                contTempBool += 1
                pilaOperandos.append(temp)
                pilaTipo.append(result_type)

            else:
                right_operand = pilaOperandos.pop()
                left_operand = pilaOperandos.pop()
                operator = pilaOperadores.pop()
                right_type = pilaTipo.pop()
                left_type = pilaTipo.pop()
                result_type = semCube.getValue(operator,left_type, right_type)
                
                if result_type == "error":
                    print("Error: Type mismatch")
                    exit()

                temp = memory.booleanTemporal
                existLeft = varTable.getVariable(left_operand)
                existRight = varTable.getVariable(right_operand)

                if existLeft != None:
                    left_operand = existLeft.dirV
                if existRight != None:
                    right_operand = existRight.dirV

                cuadruplos.addCuadruplo(operator, left_operand, right_operand, temp)
                contVarsTemp += 1
                memory.booleanTemporal += 1
                contTempBool += 1
                pilaOperandos.append(temp)
                pilaTipo.append(result_type)

                #Agrega cuadruplos de for si es que hay
                if pilaFor != []: 
                    global contTempInt, contIntVars
                    pilaFor.pop()
                    global contFor
                    dirV = memory.intLocal
                    memory.intLocal += 1
                    varTable.addVariable(Variable("VF" + str(contFor-1), "int", "N/A", dirV))
                    cuadruplos.addCuadruplo("=", right_operand, None, dirV)
                    contIntVars += 1
                    pilaSaltos.append(cuadruplos.contador)
                    temp = memory.booleanTemporal
                    dirVC = varTable.getVariable("VC" + str(contFor-1)).dirV
                    cuadruplos.addCuadruplo("<", dirVC, dirV,temp)
                    contVarsTemp += 1
                    memory.intTemporal += 1
                    pilaSaltos.append(cuadruplos.contador)
                    cuadruplos.addCuadruplo("GOTOF",temp, None, "N/A")
                    pilaOperandos.pop()
                    pilaTipo.pop()

    #Cuadruplos de suma y resta
    def cuadruplo_sr(self, tree):
        if len(pilaOperadores) > 0:
            global contVarsTemp,contTempInt, contTempFloat, contTempString, contTempBool 

            if len(pilaVariables) >= 4:
                pilaVariables.pop()
                right_operand = pilaVariables.pop()
                right_type = pilaTipo.pop()
                pilaVariables.pop()
                left_operand = pilaVariables.pop()
                left_type = pilaTipo.pop()
                operator = pilaOperadores.pop()
                result_type = semCube.getValue(operator,left_type, right_type)

                if result_type == "error":
                    print("Error: Type mismatch")
                    exit()

                temp = memory.intTemporal
                if result_type == "int":
                    temp = memory.intTemporal
                    memory.intTemporal += 1
                    contTempInt += 1

                elif result_type == "float":
                    temp = memory.floatTemporal
                    memory.floatTemporal += 1
                    contTempFloat += 1

                elif result_type == "string":
                    temp = memory.stringTemporal
                    memory.stringTemporal += 1
                    contTempString += 1

                elif result_type == "bool":
                    temp = memory.booleanTemporal
                    memory.booleanTemporal += 1
                    contTempBool += 1

                pilaOperandos.append(temp)
                pilaTipo.append(result_type)
                cuadruplos.addCuadruplo(operator, left_operand, right_operand,temp) 
            else:
                if pilaOperadores[-1] == "+" or pilaOperadores[-1] == "-":
                    right_operand = pilaOperandos.pop()
                    left_operand = pilaOperandos.pop()
                    right_type = pilaTipo.pop()
                    left_type = pilaTipo.pop()
                    operator = pilaOperadores.pop()
                    result_type = semCube.getValue(operator, left_type, right_type)
                    temp = -1

                    if result_type == "int":
                        temp = memory.intTemporal
                        memory.intTemporal += 1
                        contTempInt += 1

                    elif result_type == "float":
                        temp = memory.floatTemporal
                        memory.floatTemporal += 1
                        contTempFloat += 1

                    elif result_type == "string":
                        temp = memory.stringTemporal
                        memory.stringTemporal += 1
                        contTempString += 1

                    elif result_type == "boolean":
                        temp = memory.booleanTemporal
                        memory.booleanTemporal += 1
                        contTempBool += 1

                    existLeft = varTable.getVariable(left_operand)
                    existRight = varTable.getVariable(right_operand)
                    if existLeft != None:
                        left_operand = existLeft.dirV
                    if existRight != None:
                        right_operand = existRight.dirV

                    cuadruplos.addCuadruplo(operator, left_operand, right_operand,temp)
                    contVarsTemp += 1
                    pilaOperandos.append(temp)
                    pilaTipo.append(result_type)

    #Cuadruplos de multiplicacion y division
    def  cuadruplo_md(self, tree):
        if len(pilaOperadores) > 0:
            if pilaOperadores[-1] == "*" or pilaOperadores[-1] == "/":

                global contVarsTemp,contTempInt, contTempFloat, contTempString, contTempBool 

                right_operand = pilaOperandos.pop()
                left_operand = pilaOperandos.pop()
                right_type = pilaTipo.pop()
                left_type = pilaTipo.pop()
                operator = pilaOperadores.pop()
                result_type = semCube.getValue(operator, left_type, right_type)
                temp = -1

                if result_type == "int":
                    temp = memory.intTemporal
                    memory.intTemporal += 1
                    contTempInt += 1

                elif result_type == "float":
                    temp = memory.floatTemporal
                    memory.floatTemporal += 1
                    contTempFloat += 1

                elif result_type == "string":
                    temp = memory.stringTemporal
                    memory.stringTemporal += 1
                    contTempString += 1

                elif result_type == "boolean":
                    temp = memory.booleanTemporal
                    memory.booleanTemporal += 1
                    contTempBool += 1

                existLeft = varTable.getVariable(left_operand)
                existRight = varTable.getVariable(right_operand)
                if existLeft != None:
                    left_operand = existLeft.dirV
                if existRight != None:
                    right_operand = existRight.dirV

                cuadruplos.addCuadruplo(operator, left_operand, right_operand,temp)
                contVarsTemp += 1
                pilaOperandos.append(temp)
                pilaTipo.append(result_type)

    #Guardar ID en pila de operandos
    def guardar_id(self, tree):
        varName = tree.children[0].value
        var = varTable.getVariable(varName)
        if var == None:
            print("Error: Variable not defined")
            exit()
            
        pilaOperandos.append(varName)
        pilaTipo.append(var.type)
        pilaRevisarVar.append(True)

    #Guardar un int en la pila de operandos
    def guardar_int(self, tree):
        global contInt
        pilaTipo.append("int")
        exist = constTable.doesExist(int(tree.children[0].value))

        if exist == False:
            dirV = memory.memory["constante"]["int"] + contInt
            contInt += 1
            constTable.addConstant(dirV, int(tree.children[0].value), "int")
            pilaOperandos.append(dirV)
        else:
            dirV = constTable.getDirV(int(tree.children[0].value))
            pilaOperandos.append(dirV)

    #Guardar un float en la pila de operandos
    def guardar_float(self, tree):
        global contFloat
        pilaTipo.append("float")
        exist = constTable.doesExist(float(tree.children[0].value))

        if exist == False:
            dirV = memory.memory["constante"]["float"] + contFloat
            contFloat += 1
            constTable.addConstant(dirV, float(tree.children[0].value), "float")
            pilaOperandos.append(dirV)
        else:
            dirV = constTable.getDirV(float(tree.children[0].value))
            pilaOperandos.append(dirV)

    #Guardar un string en la pila de operandos
    def guardar_string(self, tree):
        global contString
        pilaTipo.append("string")
        exist = constTable.doesExist(tree.children[0].value.replace('"', ''))

        if exist == False:
            dirV = memory.memory["constante"]["string"] + contString
            contString += 1
            constTable.addConstant(dirV,tree.children[0].value.replace('"', ''), "string")
            pilaOperandos.append(dirV)
        else:
            dirV = constTable.getDirV(tree.children[0].value.replace('"', ''))
            pilaOperandos.append(dirV)

    #Guardar un booleano en la pila de operandos
    def guardar_boolean(self, tree):
        global contBool
        dirV = memory.memory["constante"]["boolean"] + contBool
        contBool += 1

        if(tree.children[0].value == "true"):
            exist = constTable.doesExist("True")
            if exist == False:
                constTable.addConstant(dirV, True, "boolean")
                pilaOperandos.append(dirV)
            else:
                dirV = constTable.getDirV("True")
                pilaOperandos.append(dirV)

        elif (tree.children[0].value == "false"):
            exist = constTable.doesExist("False")
            if exist == False:
                constTable.addConstant(dirV, False, "boolean")
                pilaOperandos.append(dirV)
            else:
                dirV = constTable.getDirV("False")
                pilaOperandos.append(dirV)

        pilaTipo.append("boolean")

    #Asignar el valor a una variable
    def np_asignacion(self, tree):
        
        #Igualar arreglos
        if len(pilaVariables) == 4:
            pilaVariables.pop()
            resultDirv = pilaVariables.pop()
            pilaVariables.pop()
            leftDirv = pilaVariables.pop()
            cuadruplos.addCuadruplo("=", resultDirv, None, leftDirv)

        elif len(pilaVariables) == 3:
            pilaVariables.pop()
            resultDirv = pilaVariables.pop()
            leftDirv = pilaVariables.pop()
            exist = varTable.getVariable(leftDirv)

            if exist == None:
                print("Error: Variable ", leftDirv, " not defined")
                exit()

            leftDirv = exist.dirV
            exist.value = resultDirv
            varTable.updateVariable(exist)
            cuadruplos.addCuadruplo("=A", resultDirv, None, leftDirv)
        else:
            varValue = pilaOperandos.pop()
            varName = pilaVariables.pop()
            varType = pilaTipo.pop()
            var = varTable.getVariable(varName)
            valueDir = -1
            
            if var.type != varType:
                print("Error: Type mismatch")
                exit()
            
            exist = varTable.getVariable(varValue)

            if exist != None:
                var.value = exist.dirV
                varValue = exist.dirV
            else:
                var.value = varValue
            varTable.updateVariable(var)
            varNameDir = varTable.getVariable(varName).dirV
            
            if int(var.size) != -1:
                dirV = pilaVariables.pop()
                cuadruplos.addCuadruplo("=", varValue, None, dirV)
            else:
                cuadruplos.addCuadruplo("=", varValue, None, varNameDir)

    def np_asignacion_2(self, tree):
        varValue = pilaOperandos.pop()
        varName = pilaVariables.pop()
        varType = pilaTipo.pop()
        var = varTable.getVariable(varName)

        if var != None:
            if var.type != varType:
                print("Error: Type mismatch")
                exit()

            var.value = varValue
            varTable.updateVariable(var)
            varNameDir = varTable.getVariable(varName).dirV
            cuadruplos.addCuadruplo("=", varValue, None, varNameDir)
        else:
            cuadruplos.addCuadruplo("=", varValue, None, varName)
    

    def end(self, tree):
        cuadruplos.addCuadruplo("END", None, None, None)
        funcMain = funcDir.getFunction("main")
        funcMain.intTemp = contTempInt
        funcMain.floatTemp = contTempFloat
        funcMain.stringTemp = contTempString
        funcMain.boolTemp = contTempBool
        funcMain.intVar = contIntVars
        funcMain.floatVar = contFloatVars
        funcMain.stringVar = contStringVars
        funcMain.booleanVar = contBoolVars
        funcMain.pointerTemp = contPointers
        funcDir.updateFunction(funcMain)

        cuadruplos.writeCuadruplos()
        constTable.writeTable()
 