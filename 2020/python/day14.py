from time import time
from classes import bcolors
import sys

if len(sys.argv) > 1 and sys.argv[1]=='test':
    archivo = "test14.txt"
else:
    archivo = "input14.txt"


def Solution(solucion, start_time, loops):
    print(f"Solution: {solucion}\t\tElapsed time: %0.10f seconds." % (time() - start_time), f" Loops: {loops}",end='\n')

def numToBinary(num):
    return "{0:b}".format(int(num)).rjust(36, '0')

def applyMask(num, mask):
    result = list(numToBinary(0))

    for index in range(0,len(mask)):
        if mask[index] == "X":
            result[index] = num[index]
        else:
            result[index] = mask[index]
    
    result = "".join(result)
    #print("\n################################################")
    #print(f"Value:\t{num}\t{int(num,2)}\nMask:\t{mask}\nResult:\t{result}\t{int(result,2)}")
    #print("################################################\n")
    
    return int(result,2)

def applyMask2(num, mask):
    result = list(numToBinary(0))

    for index in range(0,len(mask)):
        if mask[index] == "X":
            result[index] = "X"
        elif mask[index] == "0":
            result[index] = num[index]
        else:
            result[index] = "1"
            
    return SubstituirX("".join(result))


def SubstituirX(cadena):
    todos = []
    if len(cadena) == 1:
        if cadena == "X":
            todos.append("0")
            todos.append("1")
            return todos
        else:
            todos.append(cadena)
    else:
        subCadenas = SubstituirX(cadena[1:])
        if cadena[0] == "X":
            for sub in subCadenas:
                todos.append("0"+sub)
            for sub in subCadenas:
                todos.append("1"+sub)
        else:
            for sub in subCadenas:
                todos.append(cadena[0]+sub)
            
    return todos


def Part1():
    print("\nParte 1\n")
    memory = {}
    with open(archivo, 'r') as f:
        line = f.readlines()
        
        start_time = time()
        mask = ""
        for l in line:
            if l.startswith('mask'):
                mask = l.split("=")[1].strip()
                #print(mask)
            elif l.startswith('mem'):
                data = l.split("=")
                data[0] = data[0].strip().replace("mem[","").replace("]","")
                data[1] = data[1].strip()
                numBinary = numToBinary(data[1])
                #print(data)
                memory[data[0]] = applyMask(numBinary, mask)
                #memory[int(data[0])] = applyMask(numBinary, mask)

    solucion = 0
    for c in memory.keys():
        solucion += memory[c]

    Solution(solucion, start_time, 0)


def Part2():
    print("\nParte 2\n")
    memory = {}
    with open(archivo, 'r') as f:
        line = f.readlines()
        
        start_time = time()
        mask = ""
        for l in line:
            if l.startswith('mask'):
                mask = l.split("=")[1].strip()
                #print(mask)
            elif l.startswith('mem'):
                data = l.split("=")
                data[0] = data[0].strip().replace("mem[","").replace("]","")
                data[1] = data[1].strip()
                
                opciones = applyMask2(numToBinary(data[0]), mask)
                
                for opt in opciones:
                    memory[int(opt,2)] = int(data[1])

    solucion = 0
    for c in memory.keys():
        solucion += memory[c]

    Solution(solucion, start_time, 0)

Part1()
Part2()
