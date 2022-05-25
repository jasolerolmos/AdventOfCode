from dis import Instruction
from classes import Solution, Init, CleanLine
import numpy as np 
import re

day = 8

mapa = np.zeros((11,11))

listaValores = {}



def Part3():
    [lines, start_time] = Init(day, "1")
    solucion = 0
    maximo = 0
    reales = 0

    patron = re.compile(r"[\w,\"]\\x\w\w")

    for line in lines:
        line = CleanLine(line)
        #line = line[1:-1]
        total = len(line)
        hexa = len(patron.findall(line))

        slash = line.count('\\\\')
        comillas = line.count('\\"')
        parcial = total-slash-(hexa*3)-comillas - 2
        reales += parcial
        maximo += total

        #print(f"\n{parcial} {line}\tTotal: {total} Slash: {slash} Comillas: {comillas} Hexa: {hexa} Solución: {parcial}")
        print(f"\n{len(eval(line))} - {parcial}\t{line}\t{eval(line)}")

    print(f"Total: {maximo} Reales: {reales} => {maximo-reales}")


def Part1():
    [lines, start_time] = Init(day, "1")
    maximo = 0
    reales = 0

    for line in lines:
        line = CleanLine(line)

        reales += len(eval(line))
        maximo += len(line)

    print(f"Total: {maximo} Reales: {reales} => {maximo-reales}")

def Part2():
    [lines, start_time] = Init(day, "2")
    solucion = 0

Part3()
#Part2()

