from classes import Solution, Init, CleanLine
import math
import hashlib

day = 5

def Part1():
    [lines, start_time] = Init(day, "1")
    solucion = 0
    numVocalesMinimo = 3

    vocales = ['a', 'e', 'i', 'o', 'u']
    prohibidas = ['ab', 'cd', 'pq', 'xy']

    for c in range(0, len(lines)):
        cadena = CleanLine(lines[c])
        numVocales = 0
        valida = True
        
        it = 0
        while(it < len(prohibidas) and valida==True):
            if cadena.find(prohibidas[it]) >= 0:
                valida = False
            it+=1

        

        if valida:
            it = 0
            while(numVocales < numVocalesMinimo and it < len(vocales)):
                numVocales += cadena.count(vocales[it])
                it+=1

            if numVocales >= numVocalesMinimo: 
                it=0
                valida = False
                while(it<len(cadena)-1 and valida==False):
                    if cadena[it] == cadena[it+1]:
                        valida = True
                    it+=1
            else:
                valida = False
        
        if valida:
            solucion+=1
    
    Solution(solucion, start_time, 0)


def Part2():
    [lines, start_time] = Init(day, "2")
    solucion = 0


    for c in range(0, len(lines)):
        cadena = CleanLine(lines[c])
        
        it = 0
        valida = False
        while(it<len(cadena)-2 and valida==False):
            if cadena[it] == cadena[it+2]:
                valida = True
            it+=1

        if valida == True:
            it = 0
            valida = False
            while(it<len(cadena)-1 and valida==False):
                if cadena[it+2:].count(cadena[it]+cadena[it+1]) > 0 :
                    valida = True
                it+=1


        if valida:
            solucion+=1
    
    Solution(solucion, start_time, 0)
  


Part1()
Part2()