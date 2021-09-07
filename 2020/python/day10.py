from time import time
from classes import bcolors
from collections import OrderedDict as odict, Counter

start_time = time()
archivo = "day10Input.txt"
#archivo = "input.txt"
rango = 5
result = 0

def CheckPar(num1, num2, result):
    if num1 != num2 and (num1 + num2) == result:
        return True
    False

def SearchPaar(codeList, index):
    aux = list(codeList[index-rango:index])
    for idx, num1 in enumerate(aux, start=0):
        for num2 in aux[(idx+1)::]:
            if CheckPar(num1, num2, codeList[index]):
                return [codeList[index], num1, num2]
      


def CheckList(numList, resultado):
    total = 0
    range = list()
    for num in numList:
        total = total + num
        range.append(num)
        if total == resultado:
            return range
        else :
            if total > resultado:
                range = list()
                return False
    return False

def SearchRange(codeList, index):
    aux = list(codeList[0:index])
    for idx, num1 in enumerate(aux, start=0):
        range = CheckList(aux[(idx+1)::], codeList[index])
        if range:
            return min(range)+max(range)


def PartOne():
    global rango
    f = open(archivo, "r")
    joltList = [0]
    results = [0,0,0]


    for line in f:
        line = line.replace('\n', '').replace('\r', '')
        joltList.append(int(line))
    joltList.append(max(joltList)+3)
    joltList.sort()
    
    for idx, jolt in enumerate(joltList, start=0):
        if idx<(len(joltList)-1):
            #print(jolt,"=> ",(joltList[idx+1]-jolt))
            if (joltList[idx+1]-jolt) == 1:
                results[0] = results[0] + 1
            else:
                if (joltList[idx+1]-jolt) == 2:
                    results[1] = results[1] + 1
                else:
                    if (joltList[idx+1]-jolt) == 3:
                        results[2] = results[2] + 1

    return results[2]*results[0]

def Options(list, jolt):
    opt = []
    for n in list:
        if (n-jolt) == 1:
            opt.append(n)
        if (n-jolt) == 2:
            opt.append(n)
        if (n-jolt) == 3:
            opt.append(n)
    return opt

def OptionesWithIndex(list, idx):
    opt = []
    for n in range(1,4):
        if (idx+n)<len(list):
            if list[idx+n]-list[idx] == 1:
                opt.append(idx+n)
            if list[idx+n]-list[idx] == 2:
                opt.append(idx+n)
            if list[idx+n]-list[idx] == 3:
                opt.append(idx+n)
    return opt

def SeeOptiones(joltList, results, idx):
    global result
    #print(joltList[idx], end=' ')
    if joltList[idx] == max(joltList):
        result = result + 1
    for o in results[idx]:
        SeeOptiones(joltList, results, o)

def PartTwo():
    f = open(archivo, "r")
    joltList = [0]
    results = []

    for line in f:
        line = line.replace('\n', '').replace('\r', '')
        joltList.append(int(line))
    joltList.append(max(joltList)+3)
    joltList.sort()
    
    for n in joltList:
        print(n," ",end='')
    print()
    
    for idx, jolt in enumerate(joltList, start=0):
        results.append(Options(joltList, jolt))
        #results.append(OptionesWithIndex(joltList, idx))

    #SeeOptiones(joltList, results, 0)

    print("Variantes: ",results)

    def dfc(D, v, M={}):
        "Memoized depth first counter"
        if v in M:
            return M[v]
        elif D[v]:
            M[v] = sum(dfc(D, x, M) for x in D[v])
            return M[v]
        else:
            return 1
    print(len(results))
    #return dfc(results, 0)


print(f"\n{bcolors.FAIL}Solución 1:",f"{bcolors.OKGREEN}",PartOne(),f"{bcolors.ENDC}")
print("Elapsed time: %0.10f seconds." % (time() - start_time))
start_time = time()
print(f"{bcolors.FAIL}Solución 2:",f"{bcolors.OKGREEN}",PartTwo(),f"{bcolors.ENDC}")
print("Elapsed time: %0.10f seconds." % (time() - start_time))
