from time import time
from classes import bcolors

start_time = time()
archivo = "day9Input.txt"
#archivo = "input.txt"
rango = 5

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
    codeList = []
    errors = list()
    for line in f:
        line = line.replace('\n', '').replace('\r', '')
        codeList.append(int(line))

    rango = 25

    #for index in range(0, rango):
        #print("["+str(codeList[index])+"]")

    for index in range(rango, len(codeList)):
        #print("["+str(codeList[index])+"]\t", end='')
        result = SearchPaar(codeList, index)
        if result == None:
            #print(f"{bcolors.FAIL}ERROR{bcolors.ENDC}")
            errors.append(codeList[index])
        #else:
            #print(f"{bcolors.OKGREEN}"+str(result[1])+f"{bcolors.ENDC}","+",f"{bcolors.OKGREEN}"+str(result[2])+f"{bcolors.ENDC}")
    return errors[0]

def PartTwo():
    global rango
    f = open(archivo, "r")
    codeList = []
    errors = list()
    result = 0
    for line in f:
        line = line.replace('\n', '').replace('\r', '')
        codeList.append(int(line))

    rango = 25
    #for index in range(0, rango):
        #print("["+str(codeList[index])+"]")

    for index in range(rango, len(codeList)):
        #print("["+str(codeList[index])+"]\t", end='')
        result = SearchPaar(codeList, index)
        if result == None:
        #    print(f"{bcolors.FAIL}ERROR{bcolors.ENDC}")
            errors.append(SearchRange(codeList, index))
        #else:
        #    print(f"{bcolors.OKGREEN}"+str(result[1])+f"{bcolors.ENDC}","+",f"{bcolors.OKGREEN}"+str(result[2])+f"{bcolors.ENDC}")
    return errors[0]


print(f"\n{bcolors.OKBLUE}Solución 1:",f"{bcolors.OKGREEN}",PartOne(),f"{bcolors.ENDC}")
print("Elapsed time: %0.10f seconds." % (time() - start_time))
start_time = time()
print(f"{bcolors.OKBLUE}Solución 2:",f"{bcolors.OKGREEN}",PartTwo(),f"{bcolors.ENDC}")
print("Elapsed time: %0.10f seconds." % (time() - start_time))