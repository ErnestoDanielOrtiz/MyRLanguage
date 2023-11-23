import ast
from NeuralgicPoints import *
from VirtualMemory import *
from FunctionDirectory import *
from VariableTable import *
from SpecialFunctions import *
import time 


# Direcciones base locales y tetmporales
dirIntVar = memory.memory['local']['int']
dirFloatVar = memory.memory['local']['float']
dirStringVar = memory.memory['local']['string']
dirBoolVar = memory.memory['local']['bool']
dirIntTemp = memory.memory['temporal']['int']
dirFloatTemp = memory.memory['temporal']['float']
dirStringTemp = memory.memory['temporal']['string']
dirBoolTemp = memory.memory['temporal']['bool']
dirPointerTemp = memory.memory['temporal']['pointer']

memoriaVirtual = memory.virtualMemory

memorias = [] #Memorias virtuales
goBack = []
cuadruplos = []
tablaConst = {}
tablaGlobal = VariableTable()
tablaGlob = tablaGlobal.globales
cuadPointer = 0
tablaVariable = []
dirFunc = {}
pilaContexto = ["global"]
onFunc = False

def readConstantes():
    c = open('Constantes.txt', 'r')
    constantes = c.readlines()
    for constante in constantes:
        dirV,val, typ = constante.split(",")
        dirV = dirV.split('[')[1]
        dirV = int(dirV)
        typ = typ.split(']')[0]
        typ = typ[2:-1]
        if typ == 'int':
            val = int(val)
        elif typ == 'float':
            val = float(val)
        elif typ == 'string':
            val = val[2:-1]
        elif typ == 'boolean':
            if val == ' True':
                val = True
            else:
                val = False
        tablaConst[dirV] = [val, typ]

def readCuadruplos():
    c = open('cuadruplos.txt', 'r')
    cuadrups = c.readlines()
    #Borra \n de las lineas
    cuadrups = [x.strip() for x in cuadrups]
    for cuadruplo in cuadrups:
        cuad = ast.literal_eval(cuadruplo)
        cuadruplos.append(cuad)

#Llenar memria virtual con variables y temporales
def fillMemory(funcName):
    func = dirFunc[funcName]

    if func.intVar > 0:
        for i in range(func.intVar):
            memoriaVirtual[dirIntVar + i] = None

    if func.floatVar > 0:
        for i in range(func.floatVar):
            memoriaVirtual[dirFloatVar + i] = None

    if func.stringVar > 0:
        for i in range(func.stringVar):
            memoriaVirtual[dirStringVar + i] = None

    if func.booleanVar > 0:
        for i in range(func.booleanVar):
            memoriaVirtual[dirBoolVar + i] = None

    if func.intTemp > 0:
        for i in range(func.intTemp):
            memoriaVirtual[dirIntTemp + i] = None

    if func.floatTemp > 0:
        for i in range(func.floatTemp):
            memoriaVirtual[dirFloatTemp + i] = None

    if func.stringTemp > 0:
        for i in range(func.stringTemp):
            memoriaVirtual[dirStringTemp + i] = None

    if func.booleanTemp > 0:
        for i in range(func.boolTemp):
            memoriaVirtual[dirBoolTemp + i] = None

    if func.pointerTemp > 0:
        for i in range(func.pointerTemp):
            memoriaVirtual[dirPointerTemp + i] = None

def saveMemory():
    memorias.append(memoriaVirtual.copy())
    memoriaVirtual.clear()

def findMain():
    global cuadPointer
    for cuadruplo in cuadruplos:
        if cuadruplo[0] == 'GOTO-MAIN':
            cuadPointer = cuadruplo[3]
            break

def myR():

    global cuadPointer, memoriaVirtual, goBack, onFunc

    operator = cuadruplos[cuadPointer][0]
    first = False

    while operator != 'END':
        operator = cuadruplos[cuadPointer][0]
        left = cuadruplos[cuadPointer][1]
        right = cuadruplos[cuadPointer][2]
        result = cuadruplos[cuadPointer][3]

        if operator != '=' and first != True :
            first = True
            findMain()
            fillMemory('main')

        elif operator == 'GOTO-MAIN':
            fillMemory("main")
            cuadPointer = int(result)

        elif operator == 'ERA':
            saveMemory()
            fillMemory(result)
            pilaContexto.append(result)
            cuadPointer += 1

        elif operator == 'PARAM':
            if left in tablaConst:
                memoriaVirtual[result] = tablaConst[left][0]
            else:
                memoriaVirtual[result] = memorias[len(memorias)-1][left]
            cuadPointer += 1

        elif operator == 'GOSUB':
            if result != "special":
                goBack.append(cuadPointer + 1)
                cuadPointer = int(result)
            else:
                if onFunc == False:
                    goBack.append(cuadPointer + 1)
                    specialFuncs(pilaContexto[-1])
                    onFunc = True
                else:
                    cuadPointer = goBack.pop()
                    memoriaVirtual = memorias.pop()
                    onFunc = False
                    pass
            
        elif operator == 'ENDFUNC':
            cuadPointer = goBack.pop()
            memoriaVirtual = memorias.pop()
            pilaContexto.pop()

        elif operator == '+':
            if left >= 20000 and left < 29000:
                val,type = tablaConst[left]
                if type == 'int':
                    left = int(val)
                elif type == 'float':
                    left = float(val)
                elif type == 'string':
                    left = val
                elif type == 'boolean':
                    left = val

            elif left >= 1000 and left < 9000:
                var = tablaDeVariables.getVariableGlobalID(left)
                left = var.value

            else:
                left = memoriaVirtual[left]
            if right >= 20000 and right < 29000:
                val,type = tablaConst[right]
                if type == 'int':
                    right = int(val)
                elif type == 'float':
                    right = float(val)
                elif type == 'string':
                    right = val
                elif type == 'boolean':
                    right = val

            elif right >= 1000 and right < 9000:
                var = tablaDeVariables.getVariableGlobalID(right)
                right = var.value
            else:
                right = memoriaVirtual[right]

            memoriaVirtual[result] = left + right
            cuadPointer += 1

        elif operator == '+A':
            if left >= 20000 and left < 29000:
                val,type = tablaConst[left]
                if type == 'int':
                    left = int(val)
                elif type == 'float':
                    left = float(val)
                elif type == 'string':
                    left = val
                elif type == 'boolean':
                    left = val

            elif left >= 1000 and left < 9000:
                var = tablaDeVariables.getVariableGlobalID(left)
                left = var.value
            else:
                left = memoriaVirtual[left]

            memoriaVirtual[result] = left + int(right)
            cuadPointer += 1

        elif operator == '-':
            if left >= 20000 and left < 29000:
                val,type = tablaConst[left]
                if type == 'int':
                    left = int(val)
                elif type == 'float':
                    left = float(val)
                elif type == 'string':
                    left = val
                elif type == 'boolean':
                    left = val
            else:
                left = memoriaVirtual[left]

            if right >= 20000 and right < 29000:
                val,type = tablaConst[right]
                if type == 'int':
                    right = int(val)
                elif type == 'float':
                    right = float(val)
                elif type == 'string':
                    right = val
                elif type == 'boolean':
                    right = val
            else:
                right = memoriaVirtual[right]

            memoriaVirtual[result] = left - right
            cuadPointer += 1

        elif operator == '*':
            if left >= 20000 and left < 29000:
                val,type = tablaConst[left]
                if type == 'int':
                    left = int(val)
                elif type == 'float':
                    left = float(val)
                elif type == 'string':
                    left = val
                elif type == 'boolean':
                    left = val
            else:
                left = memoriaVirtual[left]

            if right >= 20000 and right < 29000:
                val,type = tablaConst[right]
                if type == 'int':
                    right = int(val)
                elif type == 'float':
                    right = float(val)
                elif type == 'string':
                    right = val
                elif type == 'boolean':
                    right = val
            else:
                right = memoriaVirtual[right]

            memoriaVirtual[result] = left * right
            cuadPointer += 1

        elif operator == '/':
            if left >= 20000 and left < 29000:
                val,type = tablaConst[left]
                if type == 'int':
                    left = int(val)
                elif type == 'float':
                    left = float(val)
                elif type == 'string':
                    left = val
                elif type == 'boolean':
                    left = val
            else:
                left = memoriaVirtual[left]

            if right >= 20000 and right < 29000:
                val,type = tablaConst[right]
                if type == 'int':
                    right = int(val)
                elif type == 'float':
                    right = float(val)
                elif type == 'string':
                    right = val
                elif type == 'boolean':
                    left = val
            else:
                right = memoriaVirtual[right]

            if right == 0:
                print("ERROR: Division by zero")
                exit()

            memoriaVirtual[result] = left / right
            cuadPointer += 1

        elif operator == '=':
            if result >= 1000 and result < 9000:
                if left >= 20000 and left < 29000:
                    val,type = tablaConst[left]
                    if type == 'int':
                        left = int(val)
                    elif type == 'float':
                        left = float(val)
                    elif type == 'string':
                        left = val
                    elif type == 'boolean':
                        left = val
                elif left >= 1000 and left < 9000:
                    left = tablaGlobal[left]
                else:
                    left = memoriaVirtual[left]

                var = tablaDeVariables.getVariableGlobalID(result)
                var.value = left
                tablaDeVariables.updateVariableGlobal(var)

            elif result >= 42000:
                if left >= 20000 and left < 29000:
                    val,type = tablaConst[left]
                    if type == 'int':
                        left = int(val)
                    elif type == 'float':
                        left = float(val)
                    elif type == 'string':
                        left = val
                    elif type == 'boolean':
                        left = val

                elif left >= 1000 and left < 9000:
                    left = tablaGlobal[left]
                elif left >= 42000:
                    dirLeft = memoriaVirtual[left]
                    left = memoriaVirtual[dirLeft]
                else:
                    left = memoriaVirtual[left]
                varResult = memoriaVirtual[result]
                memoriaVirtual[varResult] = left
            else:
                if left >= 20000 and left < 29000:
                    val,type = tablaConst[left]
                    if type == 'int':
                        left = int(val)
                    elif type == 'float':
                        left = float(val)
                    elif type == 'string':
                        left = val
                    elif type == 'boolean':
                        left = val
                elif left >= 1000 and left < 9000:
                    left = tablaGlobal[left]
                else:
                    left = memoriaVirtual[left]

                memoriaVirtual[result] = left
            cuadPointer += 1

        elif operator == '++':
            if left >= 20000 and left < 29000:
                val,type = tablaConst[left]
                if type == 'int':
                    left = int(val)
                elif type == 'float':
                    left = float(val)
                elif type == 'string':
                    left = val
                elif type == 'boolean':
                    left = val
            else:
                left = memoriaVirtual[left]
            if right >= 20000 and right < 29000:
                val,type = tablaConst[right]
                if type == 'int':
                    right = int(val)
                elif type == 'float':
                    right = float(val)
                elif type == 'string':
                    right = val
                elif type == 'boolean':
                    right = val
            else:
                right = memoriaVirtual[right]
            memoriaVirtual[result] = left + right
            cuadPointer += 1
        elif operator == '--':
            if left >= 20000 and left < 29000:
                val,type = tablaConst[left]
                if type == 'int':
                    left = int(val)
                elif type == 'float':
                    left = float(val)
                elif type == 'string':
                    left = val
                elif type == 'boolean':
                    left = val
            else:
                left = memoriaVirtual[left]
            if right >= 20000 and right < 29000:
                val,type = tablaConst[right]
                if type == 'int':
                    right = int(val)
                elif type == 'float':
                    right = float(val)
                elif type == 'string':
                    right = val
                elif type == 'boolean':
                    right = val
            else:
                right = memoriaVirtual[right]
            memoriaVirtual[result] = left - right
            cuadPointer += 1
        elif operator == '==':
            if left >= 20000 and left < 29000:
                val,type = tablaConst[left]
                if type == 'int':
                    left = int(val)
                elif type == 'float':
                    left = float(val)
                elif type == 'string':
                    left = val
                elif type == 'boolean':
                    left = val
            else:
                valLeft = memoriaVirtual[left]
                if valLeft >= 42000:
                    if left >= 10000 and left < 13000:
                        left = memoriaVirtual[valLeft]
                        left = int(memoriaVirtual[left])
                else:
                    left = valLeft
            
            if right >= 20000 and right < 29000:
                val,type = tablaConst[right]
                if type == 'int':
                    right = int(val)
                elif type == 'float':
                    right = float(val)
                elif type == 'string':
                    right = val
                elif type == 'boolean':
                    right = val
            else:
                valRight = memoriaVirtual[right]
                if valRight >= 42000:
                    print(right)
                else:
                    right = valRight

            if left == right:
                memoriaVirtual[result] = True
            else:
                memoriaVirtual[result] = False
            cuadPointer += 1
        elif operator == '==A':
            if left >= 20000 and left < 29000:
                val,type = tablaConst[left]
                if type == 'int':
                    left = int(val)
                elif type == 'float':
                    left = float(val)
                elif type == 'string':
                    left = val
                elif type == 'boolean':
                    left = val
            else:
                valLeft = memoriaVirtual[left]
                if valLeft >= 42000:
                    if left >= 10000 and left < 13000:
                        left = memoriaVirtual[valLeft]
                        left = int(memoriaVirtual[left])
                else:
                    left = valLeft
            
            if right >= 20000 and right < 29000:
                val,type = tablaConst[right]
                if type == 'int':
                    right = int(val)
                elif type == 'float':
                    right = float(val)
                elif type == 'string':
                    right = val
                elif type == 'boolean':
                    right = val
            else:
                if right >= 42000:
                    right = memoriaVirtual[right]
                    right = memoriaVirtual[right]
                else:
                    right = valRight

            if left == right:
                memoriaVirtual[result] = True
            else:
                memoriaVirtual[result] = False
            cuadPointer += 1
        elif operator == '>A':
            if left >= 20000 and left < 29000:
                val,type = tablaConst[left]
                if type == 'int':
                    left = int(val)
                elif type == 'float':
                    left = float(val)
                elif type == 'string':
                    left = val
                elif type == 'boolean':
                    left = val
            else:
                valLeft = memoriaVirtual[left]
                if valLeft >= 42000:
                    if left >= 10000 and left < 13000:
                        left = memoriaVirtual[valLeft]
                        left = int(memoriaVirtual[left])
                else:
                    left = valLeft
            
            if right >= 20000 and right < 29000:
                val,type = tablaConst[right]
                if type == 'int':
                    right = int(val)
                elif type == 'float':
                    right = float(val)
                elif type == 'string':
                    right = val
                elif type == 'boolean':
                    right = val
            else:
                if right >= 42000:
                    right = memoriaVirtual[right]
                    right = memoriaVirtual[right]
                else:
                    right = valRight

            if left > right:
                memoriaVirtual[result] = True
            else:
                memoriaVirtual[result] = False
            cuadPointer += 1
        elif operator == '<A':
            if left >= 20000 and left < 29000:
                val,type = tablaConst[left]
                if type == 'int':
                    left = int(val)
                elif type == 'float':
                    left = float(val)
                elif type == 'string':
                    left = val
                elif type == 'boolean':
                    left = val
            else:
                valLeft = memoriaVirtual[left]
                if valLeft >= 42000:
                    if left >= 10000 and left < 13000:
                        left = memoriaVirtual[valLeft]
                        left = int(memoriaVirtual[left])
                else:
                    left = valLeft
            
            if right >= 20000 and right < 29000:
                val,type = tablaConst[right]
                if type == 'int':
                    right = int(val)
                elif type == 'float':
                    right = float(val)
                elif type == 'string':
                    right = val
                elif type == 'boolean':
                    right = val
            else:
                if right >= 42000:
                    right = memoriaVirtual[right]
                    right = memoriaVirtual[right]
                else:
                    right = valRight

            if left < right:
                memoriaVirtual[result] = True
            else:
                memoriaVirtual[result] = False
            cuadPointer += 1
        elif operator == '<':
            if left >= 20000 and left < 29000:
                val,type = tablaConst[left]
                if type == 'int':
                    left = int(val)
                elif type == 'float':
                    left = float(val)
                elif type == 'string':
                    left = val
                elif type == 'boolean':
                    left = val
            else:
                left = memoriaVirtual[left]
            if right >= 20000 and right < 29000:
                val,type = tablaConst[right]
                if type == 'int':
                    right = int(val)
                elif type == 'float':
                    right = float(val)
                elif type == 'string':
                    right = val
                elif type == 'boolean':
                    right = val
            else:
                right = memoriaVirtual[right]
            if left < right:
                memoriaVirtual[result] = True
            else:
                memoriaVirtual[result] = False
            cuadPointer += 1
        elif operator == '>':
            if left >= 20000 and left < 29000:
                val,type = tablaConst[left]
                if type == 'int':
                    left = int(val)
                elif type == 'float':
                    left = float(val)
                elif type == 'string':
                    left = val
                elif type == 'boolean':
                    left = val
            else:
                left = memoriaVirtual[left]
            if right >= 20000 and right < 29000:
                val,type = tablaConst[right]
                if type == 'int':
                    right = int(val)
                elif type == 'float':
                    right = float(val)
                elif type == 'string':
                    right = val
                elif type == 'boolean':
                    right = val
            else:
                right = memoriaVirtual[right]
            if left > right:
                memoriaVirtual[result] = True
            else:
                memoriaVirtual[result] = False
            cuadPointer += 1
        elif operator == '<=':
            if left >= 20000 and left < 29000:
                val,type = tablaConst[left]
                if type == 'int':
                    left = int(val)
                elif type == 'float':
                    left = float(val)
                elif type == 'string':
                    left = val
                elif type == 'boolean':
                    left = val
            else:
                left = memoriaVirtual[left]
            if right >= 20000 and right < 29000:
                val,type = tablaConst[right]
                if type == 'int':
                    right = int(val)
                elif type == 'float':
                    right = float(val)
                elif type == 'string':
                    right = val
                elif type == 'boolean':
                    right = val
            else:
                right = memoriaVirtual[right]
            if left <= right:
                memoriaVirtual[result] = True
            else:
                memoriaVirtual[result] = False
            cuadPointer += 1
        elif operator == '>=':
            if left >= 20000 and left < 29000:
                val,type = tablaConst[left]
                if type == 'int':
                    left = int(val)
                elif type == 'float':
                    left = float(val)
                elif type == 'string':
                    left = val
                elif type == 'boolean':
                    left = val
            else:
                left = memoriaVirtual[left]
            if right >= 20000 and right < 29000:
                val,type = tablaConst[right]
                if type == 'int':
                    right = int(val)
                elif type == 'float':
                    right = float(val)
                elif type == 'string':
                    right = val
                elif type == 'boolean':
                    right = val
            else:
                right = memoriaVirtual[right]
            if left >= right:
                memoriaVirtual[result] = True
            else:
                memoriaVirtual[result] = False
            cuadPointer += 1
        elif operator == '!=':
            if left >= 20000 and left < 29000:
                val,type = tablaConst[left]
                if type == 'int':
                    left = int(val)
                elif type == 'float':
                    left = float(val)
                elif type == 'string':
                    left = val
                elif type == 'boolean':
                    left = val
            else:
                left = memoriaVirtual[left]
            if right >= 20000 and right < 29000:
                val,type = tablaConst[right]
                if type == 'int':
                    right = int(val)
                elif type == 'float':
                    right = float(val)
                elif type == 'string':
                    right = val
                elif type == 'boolean':
                    right = val
            else:
                right = memoriaVirtual[right]
            if left != right:
                memoriaVirtual[result] = True
            else:
                memoriaVirtual[result] = False
            cuadPointer += 1
        elif operator == 'GOTOF':
            if left >= 20000 and left < 29000:
                val,type = tablaConst[left]
                if type == 'int':
                    left = int(val)
                elif type == 'float':
                    left = float(val)
                elif type == 'string':
                    left = val
                elif type == 'boolean':
                    left = val
            else:
                left = memoriaVirtual[left]
            if left == False:
                cuadPointer = result
            else:
                cuadPointer += 1
        elif operator == 'GOTO':
            cuadPointer = result
        elif operator == 'READ':
            if result >= 1000 and result < 9000:
                var = tablaDeVariables.getVariableGlobalID(result)
                var.value = input( )
                tablaDeVariables.updateVariableGlobal(var)
            else:
                if result >= 10000 and result < 13000:
                    memoriaVirtual[result] = int(input( ))
                elif result >= 13000 and result < 15000:
                    memoriaVirtual[result] = float(input( ))
                elif result >= 15000 and result < 17000:
                    memoriaVirtual[result] = input( )
                elif result >= 17000 and result < 19000:
                    if input( ) == 'True':
                        memoriaVirtual[result] = True
                    else:
                        memoriaVirtual[result] = False
            cuadPointer += 1
        elif operator == 'and':
            if left >= 20000 and left < 29000:
                val,type = tablaConst[left]
                if type == 'int':
                    left = int(val)
                elif type == 'float':
                    left = float(val)
                elif type == 'string':
                    left = val
                elif type == 'boolean':
                    left = val
            else:
                left = memoriaVirtual[left]
            if right >= 20000 and right < 29000:
                val,type = tablaConst[right]
                if type == 'int':
                    right = int(val)
                elif type == 'float':
                    right = float(val)
                elif type == 'string':
                    right = val
                elif type == 'boolean':
                    right = val
            else:
                right = memoriaVirtual[right]
            if left and right:
                memoriaVirtual[result] = True
            else:
                memoriaVirtual[result] = False
            cuadPointer += 1
        elif operator == 'or':
            if left >= 20000 and left < 29000:
                val,type = tablaConst[left]
                if type == 'int':
                    left = int(val)
                elif type == 'float':
                    left = float(val)
                elif type == 'string':
                    left = val
                elif type == 'boolean':
                    left = val
            else:
                left = memoriaVirtual[left]
            if right >= 20000 and right < 29000:
                val,type = tablaConst[right]
                if type == 'int':
                    right = int(val)
                elif type == 'float':
                    right = float(val)
                elif type == 'string':
                    right = val
                elif type == 'boolean':
                    right = val
            else:
                right = memoriaVirtual[right]
            if left or right:
                memoriaVirtual[result] = True
            else:
                memoriaVirtual[result] = False
            cuadPointer += 1
        elif operator == 'not':
            if left >= 20000 and left < 29000:
                val,type = tablaConst[left]
                if type == 'int':
                    left = int(val)
                elif type == 'float':
                    left = float(val)
                elif type == 'string':
                    left = val
                elif type == 'boolean':
                    left = val
            else:
                left = memoriaVirtual[left]
            if left == False:
                memoriaVirtual[result] = True
            else:
                memoriaVirtual[result] = False
            cuadPointer += 1
        elif operator == 'PRINT':
            if result >= 20000 and result < 29000:
                val,type = tablaConst[result]
                if type == 'int':
                    result = str(int(val))
                elif type == 'float':
                    result = str(float(val))
                elif type == 'string':
                    result = val
                elif type == 'boolean':
                    result = val
            elif result >= 1000 and result < 9000:
                var = tablaDeVariables.getVariableGlobalID(result)
                result = var.value
            elif result >= 42000:
                pointer = memoriaVirtual[result]
                result = memoriaVirtual[pointer]
            else:
                result = memoriaVirtual[result]
            print(result)
            cuadPointer += 1
        elif operator == '=A':
            memoriaVirtual[result] = left
            cuadPointer += 1
        elif operator == 'VER':
            if left >= 20000 and left < 29000:
                val,type = tablaConst[left]
                if type == 'int':
                    left = int(val)
                elif type == 'float':
                    left = float(val)
                elif type == 'string':
                    left = val
                elif type == 'boolean':
                    left = val
            else:
                left = memoriaVirtual[left]
            if result >= 20000 and result < 29000:
                val,type = tablaConst[result]
                if type == 'int':
                    result = int(val)
                elif type == 'float':
                    result = float(val)
                elif type == 'string':
                    result = val
                elif type == 'boolean':
                    result = val
            else:
                result = memoriaVirtual[result]

            if left < 0 or left >= result:
                print('Error: Index out of range')
                exit()
            cuadPointer += 1
        elif operator == 'RETURN':
            if result >= 20000 and result < 29000:
                val,type = tablaConst[result]
                if type == 'int':
                    result = int(val)
                elif type == 'float':
                    result = float(val)
                elif type == 'string':
                    result = val
                elif type == 'boolean':
                    result = val
            else:
                result = memoriaVirtual[result]
            tablaGlobal[left] = result
            cuadPointer += 1
        
def suma(left,right):
    return left + right

def virtualMachine():
    global tablaVariables, dirFunc
    tablaVariables = tablaDeVariables
    dirFunc = funcDirectory.funcDirectory

    readConstantes()
    readCuadruplos()
    myR()
