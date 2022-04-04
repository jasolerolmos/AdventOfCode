from libs.functions import *
import numpy as np 

day = 5

mapa = np.zeros((11,11))

def Direction(line):
    pa = line[0].split(",")
    pb = line[1].split(",")
    if pa[0] == pb[0]: #Vertical
        print("\tVertical")
        if pa[1] < pb[1]:
            print(f"\t\tDesde {pa} a {pb}")
            setRoute(pa, pb, 1)
        else:
            print(f"\t\tDesde {pb} a {pa}")
            setRoute(pb, pa, 1)
    else:
        print("\tHorizontal")
        if pa[0] < pb[0]:
            print(f"\t\tDesde {pa} a {pb}")
            setRoute(pa, pb, 0)
        else:
            print(f"\t\tDesde {pb} a {pa}")
            setRoute(pb, pa, 0)


def setRoute(fr, to, way):
    if way == 0: #Horizontal
        for c in range(int(to[0]) - int(fr[0] + 1)):
            print(f"\t\t => {c+int(fr[0])}, {fr[1]}")
            mapa[int(fr[1])][(c+int(fr[0]))] = 1
    
    if way == 1: #Horizontal
        for c in range(int(to[1]) - int(fr[1]) + 1):
            print(f"\t\t => {c+int(fr[1])}, {fr[0]}")
            mapa[(c+int(fr[1]))][int(fr[0])] = 1





def Part1():
    [lines, start_time] = Init(day, "1")
    solucion = 0


    print(mapa)


    for line in lines:
        line = CleanLine(line)
        print(f"{line}")
        line = line.split(" -> ")
        pa = line[0].split(",")
        pb = line[1].split(",")
        if pa[0] == pb[0] or pa[1] == pb[1]:
            Direction(line)
        #print(pa, pb)
        print()


    print(mapa)


    Solution(solucion, start_time, 0)

def Part2():
    [lines, start_time] = Init(day, "2")
    solucion = 0

    Solution(solucion, start_time, 0)

Part1()
#Part2()