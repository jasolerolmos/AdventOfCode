from time import time
from classes import bcolors
from math import gcd
import sys

if len(sys.argv) > 1 and sys.argv[1]=='test':
    archivo = "day13test.txt"
else:
    archivo = "day13Input.txt"

salto = pow(10, 14)
print(f"Salto: {salto}")

def MCM(a):
    lcm = a[0]
    for i in a[1:]:
        lcm = lcm * i // gcd(lcm, i)
    return lcm

def msgTiempo(minuto, start_time, saltoTiempo):
    print(f"{bcolors.OKCYAN}", end='')
    print(' {:>20}'.format(minuto), end='')
    print(f"{bcolors.ENDC}", end='')
    print(f"\n\t\tSalto: {time() - saltoTiempo}" + f"\n\t\tTotal: {(time() -start_time)}", end='\n')

def Solution(solucion, start_time, loops):
    print(f"Solution: {solucion}\t\tElapsed time: %0.10f seconds." % (time() - start_time), f" Loops: {loops}",end='\n')

def Part1():
    print("\nParte 1\n")
    lineaBus = 0
    busDepart = 0
    with open(archivo, 'r') as f:
        line = f.readlines()
        timestamp = int(line[0].replace('\n', '').replace('\r', ''))
        buses = line[1].replace('\n', '').replace('\r', '')
        ids = []
        for id in buses.split(','):
            if id!='x':
                ids.append(int(id))
        print(ids)
        ids = sorted(ids)
        for minuto in range(timestamp,timestamp+ids[len(ids)-1]):
            if minuto == timestamp:
                print(f"{bcolors.OKBLUE}{minuto}{bcolors.ENDC}\t", end='')
            else:
                print(f"{minuto}\t", end='')
            for busId in ids:
                if minuto % busId == 0:
                    print(f"\tD", end='')
                    if minuto>=timestamp:
                        lineaBus = busId
                        busDepart = minuto
                else:
                    print(f"\t.", end='')

            if lineaBus > 0:
                print()
                break
            print()
        print(f"Bus: {lineaBus}\nTime to wait: {busDepart-timestamp}\nCode: {busId*(busDepart-timestamp)}")

def Part2():
    with open(archivo, 'r') as f:
        line = f.readlines()
        buses = line[1].replace('\n', '').replace('\r', '')
        ids = buses.split(',')
        
        start_time = time()
        saltoTiempo = time()
        limit = salto
        
        buscando = True
        minuto = int(ids[0])
        loops = 0
        while buscando:
            minuto += int(ids[0])
            if minuto % int(ids[0]) == 0:
                buscando = False
                for index, busId in enumerate(ids):
                    if busId != 'x' and (minuto+index) % int(busId) != 0:
                        buscando = True
                        break

            if minuto > limit:
                msgTiempo(minuto, start_time, saltoTiempo)
                limit += salto
                saltoTiempo = time()
            loops += 1

    #Solution(minuto, start_time, loops)

def Part2Alt1():
    print("\nParte 2, Alternativa 1\n")
    with open(archivo, 'r') as f:
        line = f.readlines()
        ids = line[1].replace('\n', '').replace('\r', '').split(',')
        
        start_time = time()
        saltoTiempo = time()
        limit = salto

        buscando = True
        maximo = 0
        loops = 0
        for id in ids:
            if id!='x' and maximo < int(id):
                maximo = int(id)
        posMaximo = ids.index(str(maximo))
        
        minuto = maximo
        while buscando:
            minuto += maximo
            if (minuto-posMaximo) % int(ids[0]) == 0:
                buscando = False
                for index, busId in enumerate(ids):
                    if busId != 'x' and (minuto+index-posMaximo) % int(busId) != 0:
                        buscando = True
                        break

            if minuto > limit:
                msgTiempo(minuto, start_time, saltoTiempo)
                limit += salto
                saltoTiempo = time()
            loops += 1
            
    Solution(minuto-posMaximo, start_time, loops)

def Part2Alt2(): # Mejor Forma.
    print("\nParte 2, Alternativa 2\n")
    start_time = time()
    machtes = []
    with open(archivo, 'r') as f:
        line = f.readlines()
        buses = line[1].replace('\n', '').replace('\r', '')
        ids = buses.split(',')

        start_time = time()
        saltoTiempo = time()
        limit = salto
        
        buscando = True
        
        machtes = [int(ids[0])]
        minuto = int(ids[0])
        loops = 0
        while buscando:
            minuto += MCM(machtes)
            
            for index, busId in enumerate(ids):
                if busId != 'x' and (minuto+index) % int(busId) == 0 and int(busId) not in machtes:
                    machtes.append(int(busId))

            if len(machtes) == len(ids) - ids.count('x') :
                buscando = False
            
            
            if minuto > limit:
                msgTiempo(minuto, start_time, saltoTiempo)
                limit += salto
                saltoTiempo = time()
            loops += 1
            
    Solution(minuto, start_time, loops)

Part1()
Part2Alt2()
Part2Alt1()
