from time import time
from classes import bcolors

start_time = time()
archivo = "day12Input.txt"

data = []

def Direccion(n):
    print()

def Part1():
    rosaVientos = {0: 'E', 1: 'S', 2: 'W', 3: 'N'}

    direccion = 0
    longitud = 0
    latitud = 0

    with open(archivo, 'r') as f:
        line = f.readlines()
        for l in line:
            l = l.replace('\n', '').replace('\r', '')
            action = l[0]
            num = int(l[1:])
            if action == 'L' or action == 'R':
                giro = num/90
                if action == 'L':
                    giro = giro * -1

                direccion += giro
                if direccion>=4:
                    direccion -= 4
                elif direccion<0:
                    direccion +=4

            elif action == 'F' and direccion == 0 or action == 'E':
                longitud += num
            elif action == 'F' and direccion == 1 or action == 'S':
                latitud -= num
            elif action == 'F' and direccion == 2 or action == 'W':
                longitud -= num
            elif action == 'F' and direccion == 3 or action == 'N':
                latitud += num
        
        print(f"Longitud: {longitud}\nLatitud: {latitud} \nManhatten Distance: {abs(latitud) + abs(longitud)}")

def Part2():
    rosaVientos = {0: 'E', 1: 'S', 2: 'W', 3: 'N'}

    wpLongitud = 10
    wpLatitud = 1
    cuadrante = 1
    longitud = 0
    latitud = 0

    with open(archivo, 'r') as f:
        line = f.readlines()
        for l in line:
            l = l.replace('\n', '').replace('\r', '')
            action = l[0]
            num = int(l[1:])
            
            if action == 'L' and num == 90:
                aux = wpLatitud
                wpLatitud = wpLongitud
                wpLongitud = aux * -1
            elif action == 'L' and num == 180:
                wpLatitud = wpLatitud * -1
                wpLongitud = wpLongitud * -1
            elif action == 'L' and num == 270:
                aux = wpLatitud
                wpLatitud = wpLongitud * -1
                wpLongitud = aux
            elif action == 'R' and num == 90:
                aux = wpLatitud
                wpLatitud = wpLongitud * -1
                wpLongitud = aux
            elif action == 'R' and num == 180:
                wpLatitud = wpLatitud * -1
                wpLongitud = wpLongitud * -1
            elif action == 'R' and num == 270:
                aux = wpLatitud
                wpLatitud = wpLongitud
                wpLongitud = aux * -1
            elif action == 'E':
                wpLongitud += num
            elif action == 'S':
                wpLatitud -= num
            elif action == 'W':
                wpLongitud -= num
            elif action == 'N':
                wpLatitud += num
            elif action == 'F':
                latitud += (wpLatitud*num)
                longitud += (wpLongitud*num)

            #print(f"\n{l}\nLongitud: {longitud}\nLatitud: {latitud}\nWpLongitud: {wpLongitud}\nWpLatitud: {wpLatitud}")
            '''
            if action == 'L' or action == 'R':
                giro = num/90
                if action == 'L':
                    giro = giro * -1

                direccion += giro
                if direccion>=4:
                    direccion -= 4
                elif direccion<0:
                    direccion +=4

            elif action == 'F' and direccion == 0:
                latitud += wpLatitud*num
                longitud += wpLongitud*num
            elif action == 'F' and direccion == 1:
                if direccion == 0 or action == 'E':
                    longitud += num
            elif action == 'F' and direccion == 1 or action == 'S':
                latitud -= num
            elif action == 'F' and direccion == 2 or action == 'W':
                longitud -= num
            elif action == 'F' and direccion == 3 or action == 'N':
                latitud += num
            '''
        
        print(f"\nLongitud: {longitud}\nLatitud: {latitud} \nManhatten Distance: {abs(latitud) + abs(longitud)}")

Part1()
Part2()