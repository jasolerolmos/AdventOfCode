from time import time
from classes import bcolors

start_time = time()
archivo = "day12Input.txt"

data = []

def Direccion(n):
    print()

rosaVientos = {0: 'E', 1: 'S', 2: 'W', 3: 'N'}
gps = {0: 0, 1: 0, 2: 0, 3:0}
barco = {0: 0, 1: 0, 2: 0, 3:0}

direccion = 0

wpEW = 10
wpNS = -1

EW = 0
NS = 0
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
            gps[0] = gps[0] + num
            EW += num
        elif action == 'F' and direccion == 1 or action == 'S':
            gps[1] = gps[1] + num
            NS -= num
        elif action == 'F' and direccion == 2 or action == 'W':
            gps[2] = gps[2] + num
            EW -= num
        elif action == 'F' and direccion == 3 or action == 'N':
            gps[3] = gps[3] + num
            NS += num

        #print(f"{action} {num} {rosaVientos.get(direccion)}", gps)
        #data.append(l)

    latitud = gps.get(1) - gps.get(3)
    longitud = gps.get(0) - gps.get(2)
    
    print(f"{EW} {NS} \nManhatten Distance: {abs(NS) + abs(EW)}")
    print(f"{longitud} {latitud} \nManhatten Distance: {abs(latitud) + abs(longitud)}")


