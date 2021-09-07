from time import time
from classes import bcolors

start_time = time()
archivo = "day11Input.txt"

data = []

with open(archivo, 'r') as f:
    line = f.readlines()
    for l in line:
        data.append(l.replace('\n', '').replace('\r', ''))

def CheckStatusPartOne(col, row, asientos):
    c = asientos[row][col]
    free = 0
    busy = 0
    for sy in range(-1,2):
        for sx in range(-1,2):
            if 0 <= (col+sx) < width and 0 <= (row+sy) < height and (sx!=0 or sy!=0):
                #if asientos[col+sx][row+sy] == "L":
                #    free = free + 1
                if asientos[row+sy][col+sx] == "#":
                    busy = busy + 1

    temporal[row][col] = c
    if c == 'L' and busy == 0:
        temporal[row][col] = '#'

    if c == '#' and busy >= 4:
        temporal[row][col] = 'L'

def QueSeVe(col, row, asientos):
    c = asientos[row][col]
    ocupado = 0
    libres = 0

    for vertical in range(row-1, -1, -1 ):
        if asientos[vertical][col] == '#':
            ocupado += 1
            break
        if asientos[vertical][col] == 'L':
            libres += 1
            break

    for vertical in range(row+1, height):
        if asientos[vertical][col] == '#':
            ocupado += 1
            break
        if asientos[vertical][col] == 'L':
            libres += 1
            break

    for horizontal in range(col-1, -1, -1 ):
        if asientos[row][horizontal] == '#':
            ocupado += 1
            break
        if asientos[row][horizontal] == 'L':
            libres += 1
            break

    for horizontal in range(col+1, width):
        if asientos[row][horizontal] == '#':
            ocupado += 1
            break
        if asientos[row][horizontal] == 'L':
            libres += 1
            break

    horizontal = col+1
    vertical = row+1
    while horizontal<width and vertical<height:
        if asientos[vertical][horizontal] == '#':
            ocupado += 1
            break
        if asientos[vertical][horizontal] == 'L':
            libres += 1
            break
        horizontal += 1
        vertical += 1

    horizontal = col-1
    vertical = row+1
    while horizontal>=0 and vertical<height:
        if asientos[vertical][horizontal] == '#':
            ocupado += 1
            break
        if asientos[vertical][horizontal] == 'L':
            libres += 1
            break
        horizontal -= 1
        vertical += 1

    horizontal = col-1
    vertical = row-1
    while horizontal>=0 and vertical>=0:
        if asientos[vertical][horizontal] == '#':
            ocupado += 1
            break
        if asientos[vertical][horizontal] == 'L':
            libres += 1
            break
        horizontal -= 1
        vertical -= 1

    horizontal = col+1
    vertical = row-1
    while horizontal<width and vertical>=0:
        if asientos[vertical][horizontal] == '#':
            ocupado += 1
            break
        if asientos[vertical][horizontal] == 'L':
            libres += 1
            break
        horizontal += 1
        vertical -= 1


    temporal[row][col] = c
    if c == 'L' and ocupado == 0:
        temporal[row][col] = '#'

    if c == '#' and ocupado >= 5:
        temporal[row][col] = 'L'

def CopyArray(orig):
    dest = []
    for idxRow, row in enumerate(orig):
        empty = []
        for idxCol, col in enumerate(row):
            empty.append(orig[idxRow][idxCol])
        dest.append(empty)
    return dest

def VerArray(array):
    for i in range (0, height): 
        for j in range (0, width):
            print(array[i][j],end='')
        print("")

def ContarOcupados(array):
    ocupado = 0
    for i in range (0, height): 
        for j in range (0, width):
            if array[i][j] == '#':
                ocupado += 1
    return ocupado

def IniciarArray():
    temporal = []
    for i in range (0, height): 
        new = []
        for j in range (0, width):
            new.append(".")
        temporal.append(new)
    return temporal

width = len(data[0])
height = len(data)

def Part1():
    origen = IniciarArray();
    global temporal
    temporal = CopyArray(data)
    #print("\nInicio")
    #VerArray(temporal)
    round = 0

    while temporal != origen:
        origen = CopyArray(temporal)
        round += 1
        #QueSeVeDebug(9,1,origen)
        #break
        for idxRow, row in enumerate(origen):
            for idxCol, col in enumerate(row):
                temporal[idxRow][idxCol] = "."
                if origen[idxRow][idxCol] == 'L' or origen[idxRow][idxCol] == '#':
                    CheckStatusPartOne(idxCol, idxRow, origen)
        
        if (temporal==origen):
            print("Part 1\n\tRonda:",round,"\n\toccupied:",ContarOcupados(temporal))


def Part2():
    global temporal
    origen = IniciarArray();
    temporal = CopyArray(data)
    #print("\nInicio")
    #VerArray(temporal)
    round = 0

    while temporal != origen:
        origen = CopyArray(temporal)
        round += 1
        #QueSeVeDebug(9,1,origen)
        #break
        for idxRow, row in enumerate(origen):
            for idxCol, col in enumerate(row):
                temporal[idxRow][idxCol] = "."
                if origen[idxRow][idxCol] == 'L' or origen[idxRow][idxCol] == '#':
                    QueSeVe(idxCol, idxRow, origen)
        
        if (temporal==origen):
            print("Part 2\n\tRonda:",round,"\n\toccupied:",ContarOcupados(temporal))

Part1();
Part2();