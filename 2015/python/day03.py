from classes import Solution, Init, CleanLine
day = 3

def Part1():
    [lines, start_time] = Init(day, "1")
    solucion1 = list()
    ejeY = 0
    ejeX = 0

    solucion1.append(f"{ejeY} {ejeX}")
    for ruta in lines:
        for direccion in range(len(ruta)):
            if ruta[direccion] == '^':
                ejeY += 1
            elif ruta[direccion] == 'v':
                ejeY -= 1
            elif ruta[direccion] == '<':
                ejeX -= 1
            elif ruta[direccion] == '>':
                ejeX += 1
            
            if f"{ejeY} {ejeX}" not in solucion1:
                solucion1.append(f"{ejeY} {ejeX}")

    Solution(len(solucion1), start_time, 0)


def Part2():
    [lines, start_time] = Init(day, "1")
    solucion1 = list()
    santa = [0,0]
    robot = [0,0]
    ejes = [0,0]

    solucion1.append(f"{ejes[0]} {ejes[1]}")
    for ruta in lines:
        for direccion in range(len(ruta)):
            if direccion % 2 == 0:
                ejes = santa
            else:
                ejes = robot

            if ruta[direccion] == '^':
                ejes[1] += 1
            elif ruta[direccion] == 'v':
                ejes[1] -= 1
            elif ruta[direccion] == '<':
                ejes[0] -= 1
            elif ruta[direccion] == '>':
                ejes[0] += 1
            
            if f"{ejes[0]} {ejes[1]}" not in solucion1:
                solucion1.append(f"{ejes[0]} {ejes[1]}")

            if direccion % 2 == 0:
                santa = ejes
            else:
                robot = ejes

    Solution(len(solucion1), start_time, 0)
  


Part1()
Part2()