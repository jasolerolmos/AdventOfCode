from classes import Solution, Init, CleanLine
import numpy as np

day = 6
size = [1000,1000]

lights = np.full((size[0],size[1]), 0)

def Part2():
    [lines, start_time] = Init(day, "1")
    solucion = 0

def CountLight(p1, p2):
    pA = [int(c) for c in p1.split(',')]
    pB = [int(c) for c in p2.split(',')]
    
    auxA = pB[0]-pA[0]+1
    auxB = pB[1]-pA[1]+1
    numLight = auxA * auxB

    return numLight

def OnOff(p1, p2, val):
    pA = [int(c) for c in p1.split(',')]
    pB = [int(c) for c in p2.split(',')]

    for y in range(pA[0],pB[0]+1):
        for x in range(pA[1],pB[1]+1):
            lights[y][x] = val

def Toggle(p1, p2):
    pA = [int(c) for c in p1.split(',')]
    pB = [int(c) for c in p2.split(',')]

    for y in range(pA[0],pB[0]+1):
        for x in range(pA[1],pB[1]+1):
            lights[y][x] = (lights[y][x] + 1) % 2
    
def LightsOn():
    sum = 0
    for y in range(0, size[0]):
        for x in range(0, size[1]):
            sum += lights[y][x]
    
    return sum


def Part1():
    [lines, start_time] = Init(day, "2")
    solucion = 0

    print(f"{lights}")
    for line in lines:
        parts = CleanLine(line).split(" ")
        if len(line.split(" ")) == 4:
            print(f"Toggle: {parts[1]} - {parts[3]}")
            CountLight(parts[1], parts[3])
            Toggle(parts[1], parts[3])
        else:
            print(f"on/off: {parts[2]} - {parts[4]}")
            CountLight(parts[2], parts[4])
            if parts[1] == 'on':
                OnOff(parts[2], parts[4], 1)
            else:
                OnOff(parts[2], parts[4], 0)

    print(f"{lights}")
    print(f"{LightsOn()}")
Part1()
