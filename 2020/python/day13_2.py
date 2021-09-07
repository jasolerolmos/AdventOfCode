from time import time
from classes import bcolors
from math import gcd

start_time = time()
archivo = "day13Input.txt"

def compute_lcm(a):
    lcm = a[0]
    for i in a[1:]:
        lcm = lcm * i // gcd(lcm, i)
    return lcm

def Part1():
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
    archivo = "day13Input.txt"
    with open(archivo, 'r') as f:
        start_time = time()
        saltoTiempo = time()
        salto = pow(10, 8)
        limit = salto

        line = f.readlines()
        ids = line[1].replace('\n', '').replace('\r', '').split(',')
        
        buscando = True
        maximo = 0
        for id in ids:
            if id!='x' and maximo < int(id):
                maximo = int(id)
        posMaximo = ids.index(str(maximo))
        
        minuto = maximo
        print(f"{ids}")
        print(f"{maximo} Pos: {posMaximo}")
        while buscando:
            minuto += maximo

            if (minuto-posMaximo) % int(ids[0]) == 0:
                buscando = False
                for index, busId in enumerate(ids):
                    if busId != 'x' and (minuto+index-posMaximo) % int(busId) != 0:
                        buscando = True
                        break

            if minuto > limit:
                print(f"{bcolors.OKCYAN}", end='')
                print(' {:>20}'.format(minuto))
                print(f"{bcolors.ENDC}", end='')
                print(f"\tTotal: {(time() -start_time)} seconds." + f"\tSalto: {time() - saltoTiempo}")
                limit += salto
                saltoTiempo = time()
            
            
    print(f"{minuto-maximo}")
    print("\t\tElapsed time: %0.10f seconds." % (time() - start_time))

def Part3(): # Mejor
    archivo = "day13Input.txt"
    start_time = time()
    machtes = []
    with open(archivo, 'r') as f:
        line = f.readlines()
        buses = line[1].replace('\n', '').replace('\r', '')
        ids = buses.split(',')
        
        buscando = True
        
        machtes = [int(ids[0])]
        minuto = int(ids[0])
        print(buses)
        while buscando:
            minuto += compute_lcm(machtes)
            
            for index, busId in enumerate(ids):
                if busId != 'x' and (minuto+index) % int(busId) == 0 and int(busId) not in machtes:
                    machtes.append(int(busId))

            if len(machtes) == len(ids) - ids.count('x') :
                buscando = False
            
            if minuto % 10000000 == 0:
                print(f"{bcolors.OKCYAN}", end='')
                print(' {:>20}'.format(minuto))
                print(f"{bcolors.ENDC}", end='')
                print("\t\tElapsed time: %0.10f seconds." % (time() - start_time))
    print(f"{minuto}")
    print("\t\tElapsed time: %0.10f seconds." % (time() - start_time))

def Part4():
    archivo = "day13test.txt"
    with open(archivo, 'r') as f:
        start_time = time()
        saltoTiempo = time()
        salto = pow(10, 11)
        limit = salto

        line = f.readlines()
        ids = line[1].replace('\n', '').replace('\r', '').split(',')
        
        buscando = True
        maximo = 0
        for id in ids:
            if id!='x' and maximo < int(id):
                maximo = int(id)
        posMaximo = ids.index(str(maximo))
        
        minuto = maximo

        print(f"{ids}")
        print(f"{maximo} Pos: {posMaximo}")
        while buscando:
            if (minuto-posMaximo) % int(ids[0]) == 0:
                buscando = False
                for index, busId in enumerate(ids):
                    if busId != 'x' and (minuto+index-posMaximo) % int(busId) != 0:
                        buscando = True
                        break

            minuto += maximo
            if minuto > limit:
                print(f"{bcolors.OKCYAN}", end='')
                print(' {:>20}'.format(minuto))
                print(f"{bcolors.ENDC}", end='')
                print(f"\tTotal: {(time() -start_time)} seconds." + f"\tSalto: {time() - saltoTiempo}")
                limit += salto
                saltoTiempo = time()
            
            
    print(f"{minuto-maximo}")
    print("\t\tElapsed time: %0.10f seconds." % (time() - start_time))

Part2()